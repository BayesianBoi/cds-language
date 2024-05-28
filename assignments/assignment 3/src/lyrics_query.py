import os
import pandas as pd
from gensim.downloader import load
from emissions_tracker import start_tracker, stop_and_save_tracker
import re
import csv
import argparse
"""
Script for query searching a word in the lyrics and finding the most similar words
"""
def preprocess_lyrics(lyrics):
    """
    Preprocessing the lyrics (converting to lowercase, removing punctuation and spaces)
    """
    lyrics = lyrics.lower()  # lowercasing
    lyrics = re.sub(r"[^\w\s]", "", lyrics)  # removing punctuation
    lyrics = lyrics.strip()  # removing spaces
    return lyrics

def load_data(file_path):
    """
    Loading spotify data set
    """
    data = pd.read_csv(file_path)
    data["text"] = data["text"].apply(preprocess_lyrics)  # applying the preprocessing to the lyrics
    data["artist"] = data["artist"].str.lower()  # lowercase the artist name
    return data

def get_similar_words(model, keyword, top_words=10, show_similarity=False):
    """
    Find the most similar words to the given keyword
    """
    try:
        similar_words = model.most_similar(keyword, topn=top_words)  # getting the top 10 words most similar words to the keyword
        if show_similarity: # if the arg has been selected, also get the similarity scores in the output and csv
            words_with_score = [f"{word} ({score:.2f})" for word, score in similar_words]  # include similarity scores + the word
            return [word for word, _ in similar_words], words_with_score  # returns both the list with only names and the one with names + score
        else:
            return [word for word, _ in similar_words], [word for word, _ in similar_words]  # only the words
    except KeyError:  # checks if the given keyword exists in the dataset
        print(f"Keyword '{keyword}' not found in the glove model")
        return [], []

def calculate_artist_song_percentage(data, artist, keywords):
    """
    Calculate the percentage of songs by the artist that contain the keyword
    """
    artist_songs = data[data["artist"] == artist] #making a list of the chosen artist's songs
    total_songs = len(artist_songs) # calculating the number of songs that the artist has
    if total_songs == 0: # makes sure that the artist is in the data set
        raise KeyError(f"Artist '{artist}' not found in the dataset")
    
    matching_songs = sum(any(keyword in song for keyword in keywords) for song in artist_songs["text"]) # checks all of the artist's songs and returns a number of songs where similar words to the chosen word is present
    percentage = (matching_songs / total_songs) * 100 # getting percentage of the songs (out of all of the artist's songs) that contain similar words to the search word
    return matching_songs, percentage, total_songs

def main(artist, keyword, top_words, show_similarity):
    # lowercase the artist and keyword arguments, so "AbBa" is the same as "ABBA"
    artist = artist.lower()
    keyword = keyword.lower()
    
    # Loading the data
    data_file = "in/spotify-songs.csv"
    data = load_data(data_file)
    print("Data loaded and preprocessed")
    
    # Finding the similar words with/without score depending on chosen argument
    similar_words_no_score, similar_words_with_score = get_similar_words(model, keyword, top_words, show_similarity)
    print(f"Similar words to '{keyword}': {similar_words_with_score}")

    # Calculate the percentage of songs containing similar words
    matching_songs, percentage, total_songs = calculate_artist_song_percentage(data, artist, similar_words_no_score)
    print(f"{percentage:.2f}% of {artist}'s songs contain words related to {keyword}")
    print(f"Total matching songs: {matching_songs} out of {total_songs} songs")

    # append the results to a csv
    output_file = "out/query_search.csv" # output
    file_exists = os.path.isfile(output_file) #checks if the folder already exists
    with open(output_file, mode="a", newline="") as file: # appending the results, so we can store for each query
        writer = csv.writer(file)
        if not file_exists: # if it does not exist, create new csv with rows
            writer.writerow(["Artist", "Keyword", "Top_words", "Similar_Words", "Matching_Songs", "Total_Songs", "Percentage"])
        writer.writerow([artist, keyword, top_words, similar_words_with_score, matching_songs, total_songs, percentage])


# Loading the glove model, we go with the 300 as it is bigger than the 50. Loading it globally, so we dont have to download it each time we are running the script
model = load("glove-wiki-gigaword-300")

if __name__ == "__main__":
    # arguments
    parser = argparse.ArgumentParser(description="Query expansion with word embeddings")
    parser.add_argument("artist", type=str, help="Name of the artist")
    parser.add_argument("keyword", type=str, help="Keyword for search")
    parser.add_argument("--top_words", type=int, default=10, help="Number of similar words (default is 10)")
    parser.add_argument("--show_similarity", action="store_false", help="Include if you want to not get the similarity scores")

    args = parser.parse_args()

    # start co2 tracker
    tracker = start_tracker()

    # run the main function
    main(args.artist, args.keyword, args.top_words, args.show_similarity)

    # stop and save emissions data
    stop_and_save_tracker(tracker, "lyrics_query")

