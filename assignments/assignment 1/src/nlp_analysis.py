import pandas as pd
import spacy
import os
from utils import calculate_metrics, remove_metadata
from codecarbon import EmissionsTracker
import matplotlib.pyplot as plt
import seaborn as sns

# Main pipeline
def main():
    output_folder = "out" # defining output folder
    os.makedirs(output_folder, exist_ok=True) # create the out folder if it does not exist
    tracker = EmissionsTracker(output_dir=output_folder, output_file="emissions_assignment1.csv") # set up the emissions tracker
    tracker.start() # starting the emission tracker

    # downloading the medium spacy NLP model
    os.system("python -m spacy download en_core_web_md")
    # loading the medium spacy model
    model = spacy.load("en_core_web_md")
    
    # path to the input folder folder
    input_folder = "in/USEcorpus"

    # sorted list of subfolders in the USEcorpus
    subfolders = sorted(os.listdir(input_folder))
    # making a dictionary to store the texts from each subfolder
    subfolder_texts = {}

    for subfolder in subfolders:
        # getting the path of the specific subfolder
        subfolder_path = os.path.join(input_folder, subfolder)

        print(f"Loading the text files in {subfolder}")
        # making a list to store the text from the files in the subfolder
        texts = []

        # open each individual text file in the specific sorted subfolder and stores these as one long string for each subfolder
        for file in sorted(os.listdir(subfolder_path)):
            file_path = os.path.join(subfolder_path, file)
            # using ISO-8859-1 which ensures that all of the files can be loaded (some of them contain characters which otherwise cannot be loaded)
            with open(file_path, "r", encoding = "ISO-8859-1") as file:
                # reading the text files and appending them to the list
                text = file.read()
                text = remove_metadata(text)
                texts.append(text)
        # storing the texts from each folder in a dictionary
        subfolder_texts[subfolder] = texts

    # make a dictionary to store metrics for each subfolder
    subfolder_metrics = {}

    # for loop that calculates the metrics for an individual folder at a time and stores it
    for subfolder, texts in subfolder_texts.items():
        print(f"Performing analysis for {subfolder}")
        
        # calculate NLP metrics for the current subfolder's texts
        subfolder_df = calculate_metrics(texts, model)
        
        # Store the dataframe from each subfolder in the dictionary
        subfolder_metrics[subfolder] = subfolder_df

    # concatenete all the dataframes for the plot comparison comparing pos between the three styles of assignments
    all_metrics_df = pd.concat(subfolder_metrics.values(), keys=subfolder_metrics.keys(), names=['Subfolder', 'Index']).reset_index(level='Subfolder')

    # some of the essay are explicitly written in specific styles: defining the subfolders which are explicitly a style: (based on the details of the data set found in the /in folder)
    personal_subfolders = ['a1', 'a3']
    formal_subfolders = ['a2', 'a4', 'b1']
    academic_subfolders = ['b4', 'b5']

    # function for defining the style of the subfolder based on the list above
    def define_style(subfolder):
        if subfolder in personal_subfolders:
            return 'Personal'
        elif subfolder in formal_subfolders:
            return 'Formal'
        elif subfolder in academic_subfolders:
            return 'Academic'
        else:
            return 'Other'

    # running the function on the df that we made
    all_metrics_df['Style'] = all_metrics_df['Subfolder'].apply(define_style)

    # remove all the subfolders that is not explicitly stated as a style
    all_metrics_df = all_metrics_df[all_metrics_df['Style'] != 'Other']

    # plotting the comparison of four different kinds of POS usage in personal, formal and academic styles
    pos_tags = ['RelFreq NOUN', 'RelFreq VERB', 'RelFreq ADJ', 'RelFreq ADV']
    
    for pos_tag in pos_tags:
        plt.figure(figsize=(10, 6))
        sns.barplot(data=all_metrics_df, x='Style', y=pos_tag, errorbar= None, palette="Blues")
        plt.title(f'Comparison of {pos_tag} between Personal, Formal, and Academic Styles')
        plt.xlabel('Style')
        plt.ylabel(pos_tag)
        plt.savefig(os.path.join(output_folder, f'{pos_tag}_comparison.png'))
        plt.show()

    # create CSV files for each subfolder in the output folder
    for subfolder, df in subfolder_metrics.items():
        output_path = os.path.join(output_folder, f"nlp_results_{subfolder}.csv")
        df.to_csv(output_path, index=False)
        print("CSV saved")

    # stop the emissions tracker and output the results
    emissions = tracker.stop()
    print(f"Total CO₂ emissions for this assignment: {emissions} kg")

if __name__ == "__main__":
    main()
