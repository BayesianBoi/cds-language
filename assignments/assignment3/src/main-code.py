import gensim.downloader as api
import numpy as np 
import pandas as pd 
import os
import scipy
import argparse
from collections import Counter
import matplotlib.pyplot as plt


def load_lyrics(file_path):
    """
    Load song lyric data from a file.
    """
    lyrics = pd.read_csv(file_path)
    return lyrics


def get_similar_words(word, model, topn=10):
    """
    Get most similar words to a given word using word embeddings model.
    """
    similar_words = []
    try:
        similar_words = model.most_similar(word, topn=topn)
    except KeyError:
        print(f"Word '{word}' not found in vocabulary.")
    return similar_words

def count_artist_songs_with_terms(artist_lyrics, expanded_query):
    """
    Count the number of songs by the artist featuring terms from the expanded query.
    """
    song_count = 0
    for song_lyrics in artist_lyrics:
        if any(term in song_lyrics for term in expanded_query):
            song_count += 1
    return song_count

def calculate_percentage(total_songs, songs_with_terms):
    """
    Calculate the percentage of songs featuring the expanded query terms.
    """
    if total_songs == 0:
        return 0
    return (songs_with_terms / total_songs) * 100

def main(artist, search_term):
    # Load song lyric data
    lyrics = load_lyrics(".." "/in/spotify-songs.csv")

   # Download or load word embedding model
    model = api.load("glove-wiki-gigaword-50")

    # Get similar words to search term
    similar_words = get_similar_words(search_term, model)

    # Expand query with similar words
    expanded_query = [search_term] + [word for word, _ in similar_words]

    # Filter artist's songs and count those featuring terms from expanded query
    artist_lyrics = lyrics[lyrics['artist'] == artist]['text'].tolist()
    total_artist_songs = len(artist_lyrics)
    songs_with_terms = count_artist_songs_with_terms(artist_lyrics, expanded_query)

    # Calculate percentage
    percentage = calculate_percentage(total_artist_songs, songs_with_terms)

    # Print results
    print(f"{percentage:.2f}% of {artist}'s songs contain words related to {search_term}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find percentage of artist's songs containing words related to a search term.")
    parser.add_argument("artist", type=str, help="Name of the artist.")
    parser.add_argument("search_term", type=str, help="Search term.")
    args = parser.parse_args()

    main(args.artist, args.search_term)