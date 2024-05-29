import pandas as pd
import matplotlib.pyplot as plt
import os
from emissions_tracker import start_tracker, stop_and_save_tracker

"""This script does plotting of the processed sentiment analysis"""
def main():
    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)  # creates out folder if it doesnt exist

    tracker = start_tracker()  # start emission tracker

    # plot emotion distribution for each season
    season_dist_file = os.path.join(output_dir, "season_dist.csv")
    data = pd.read_csv(season_dist_file)  # loading the distributions from the processed script
    for season in sorted(data["Season"].unique()):  # go through each season and plot the sentiment for that season
        season_data = data[data["Season"] == season].set_index("Emotion")  # Filter data for the current season and set index to emotion

        # Plot and save the distribution
        plt.figure(figsize=(10, 5))
        season_data["Average Score"].plot.barh() 
        plt.title(f"Emotion distribution in season {season}")
        plt.xlabel("Average score")
        plt.ylabel("Emotion")
        plt.grid(axis="x")
        plt.savefig(os.path.join(output_dir, f"{season}_dist.png"))
        plt.close()

    # Plot emotion trends over all seasons
    emotion_trends_file = os.path.join(output_dir, "emotion_trends.csv")
    data = pd.read_csv(emotion_trends_file)  # loads the trends from the processed csv
    seasons = data["Season"].unique()  # get unique seasons
    emotions = [col for col in data.columns if col != "Season"]  # get list of emotions

    plt.figure(figsize=(12, 7)) 
    for emotion in emotions:  # goes through each emotion one at a time
        plt.plot(seasons, data[emotion], label=emotion)  # plots the emotion trend
    plt.title("Emotion Trends Over Seasons") 
    plt.xlabel("Season")
    plt.ylabel("Average score")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "emotion_trends.png"))
    plt.close()

    stop_and_save_tracker(tracker, "plot_data.py")  # stop and save the emissions

if __name__ == "__main__":
    main() 
