import pandas as pd
import os
from emissions_tracker import start_tracker, stop_and_save_tracker
"""This script analyses which character had the highest relative outlet of each emotion in each season"""

def main():
    input_file = "out/processed_got_script.csv"
    output_dir = "out" 
    os.makedirs(output_dir, exist_ok=True)  # make the output folder if it doesnt exist

    tracker = start_tracker()  # start tracking emissions

    data = pd.read_csv(input_file)  # loads the data

    # make a list of the possible emotions
    possible_emotions = ["sadness", "joy", "anger", "fear", "surprise", "disgust", "neutral"]

    # find the top character per emotion for each season
    results = []
    for season in sorted(data["Season"].unique()):  # goes through each season one at a time
        season_data = data[data["Season"] == season]  # filter out the data for that specific season
        season_result = {"Season": season}  # making a directionary to store the resutls for that season

        for emotion in possible_emotions:  # goes through each emotion one at a time
            if emotion == "neutral":  # skipping the neural emotion (not very interesting)
                continue
            top_character = season_data.groupby("Name")[emotion].mean().idxmax()  # find the character with highest average score for the emotion
            season_result[emotion] = top_character  # store the top character for that emotion in the season result

        results.append(season_result)  # append the season result to the results list

    # Convert the results list to a df and save it
    results_df = pd.DataFrame(results)
    results_df.to_csv(os.path.join(output_dir, "top_characters.csv"), index=False)

    stop_and_save_tracker(tracker, "top_character.py")  # stop and save the emissions

if __name__ == "__main__":
    main()