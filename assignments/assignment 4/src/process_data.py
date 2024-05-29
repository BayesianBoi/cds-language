import pandas as pd
from transformers import pipeline
import os 
from emissions_tracker import start_tracker, stop_and_save_tracker

"""This script does sentiment analysis of GoT script"""

def load_data(filepath):
    """Loads the GoT dataset"""
    return pd.read_csv(filepath) 

def sentiment_analysis(classifier, sentences, batch_size=10):
    """Emotional classification of the script in batches"""
    results = []  # make a list to store classification results
    for i in range(0, len(sentences), batch_size):  # loop through the sentences
        batch = sentences[i:i + batch_size]  # slices the sentences list into batch sizes of 10
        print(f"Classifying batch {i//batch_size + 1}/{(len(sentences) - 1)//batch_size + 1}")  # print the current progress bar. it takes a loooong time to run, so kinda necessary
        batch = [str(sentence) for sentence in batch]  # Ensure each sentence in the batch is a string. there was one of the last sentences that wasnt recognised as a string
        results.extend(classifier(batch))  # the model classifies the current batch as a whole and adds it to the results list
    return results

def main():
    input_file = "in/Game_of_Thrones_Script.csv"
    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)  # create output if it doesn't exist

    tracker = start_tracker()  # start tracking emissions

    # loading the data
    data = load_data(input_file)

    # Setting up the model for sentiment analysis
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

    # predict emotions for each line in the dataset in batches
    data["emotions"] = sentiment_analysis(classifier, data["Sentence"].tolist())  # classify emotions and add to df

    # make a list of the possible emotions
    possible_emotions = ["sadness", "joy", "anger", "fear", "surprise", "disgust", "neutral"]

    # processes the emotions data
    for emotion in possible_emotions:  # making new columns for each of the emotions and setting them to 0
        data[emotion] = 0.0  # Make columns with float type
    for index, row in data.iterrows():  # iterate over each row in the data
        for emotion_dict in row["emotions"]:  # it goes through all of the emotions rows
            data.at[index, emotion_dict["label"]] = emotion_dict["score"]  # updates the df with the found emotion score

    # Save processed data to CSV for later analysis. I had some issues with the plotting which resulted in having to rerun the processing, so splitting them up in scripts now
    data.to_csv(os.path.join(output_dir, "processed_got_script.csv"), index=False) # this is for the extra character script that finds the character with the highest relative outlet of an emotion for a season

    # save emotion distribution for each season - for making plot that show the distribution of emotions within a season, for all of the seasons
    distributions = []  # List to store all the emotion labels for all seasons
    for season in sorted(data["Season"].unique()):  # goes through each unique season
        season_data = data[data["Season"] == season]  # filters data for the current season
        avg_emotions = season_data[possible_emotions].mean().sort_values()  # calculate the average emotions per season

        # Save distribution to list
        distribution = avg_emotions.reset_index() # making sure it is a normal column again
        distribution.columns = ["Emotion", "Average Score"] # remaning the columns
        distribution["Season"] = season # adding the numbers for the season into the df
        distributions.append(distribution) # appending that df to the list

    # save all the distributions to CSV
    pd.concat(distributions).to_csv(os.path.join(output_dir, "season_dist.csv"), index=False) # collect all the season dfs we made and convert it into one big df

    # emotion trends of all seasons - for showing the relative frequency of emotions across all seasons
    trends = []  # list to store emotions for each emotion
    for emotion in possible_emotions:  # iterate over each emotion
        trend = data.groupby("Season")[emotion].mean().reset_index()  # Calculate average emotion score per season
        trend.columns = ["Season", emotion]  # rename the columns
        trends.append(trend) # append emotion to the list

    # merge all trends into a single df
    trends_df = pd.concat(trends, axis=1) # concadenate into one df
    trends_df = trends_df.loc[:, ~trends_df.columns.duplicated()]  # removes the duplicate columns
    trends_df.to_csv(os.path.join(output_dir, "emotion_trends.csv"), index=False)

    stop_and_save_tracker(tracker, "process_data.py")  # stop emissions tracking and save the data

if __name__ == "__main__":
    main()
