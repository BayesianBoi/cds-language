import re
import pandas as pd
import spacy
import string
import os
from codecarbon import EmissionsTracker
import csv

def remove_metadata(text):
    """
    Removes the metadata in pointed brackets <> that is in most of the texts
    """
    return re.sub(r"<[^>]*>", "", text)

def process_entities(entities):
    """
    Processes the entities to remove punctuation and lowercases them. Used for later in the NLP pipeline for identifying the uniqiue entities in the text
    """
    processed_entities = []  # making a list to store the processed entities in
    punc = string.punctuation  # getting the list of punc chars from the string package
    for text, label in entities:  # as this is for post-processing after spacy has located the entities, it is important that we keep the labels for the entities
        text = text.lower()  # lowercases everything
        for char in punc:  # loop through each character in the texts and removes the defined list of symbols from the texts
            text = text.replace(char, "")
        processed_entities.append((text, label))  # saves the processed entity and the entity label
    return processed_entities

def calculate_metrics(texts, model):
    """
    Calculates the NLP metrics for a list of texts.
    """
    metrics = []  # empty list for the metrics

    for i, text in enumerate(texts, 1):  # goes through each text one at a time
        # convert the individual text into a doc (using the medium-sized model)
        doc = model(text)  # convert the text to a spacy doc

        # Calculate various NLP metrics
        num_words = len(doc)  # calculate the number of words in the text file
        num_tokens = doc.count_by(spacy.attrs.POS)  # calculate the number of tokens in the text file
        rel_freq_noun = round(num_tokens.get(spacy.parts_of_speech.NOUN, 0) / num_words * 10000, 1)  # relative number of nouns in text file per 10k words. The 0 is if didnt find any nouns in the doc
        rel_freq_verb = round(num_tokens.get(spacy.parts_of_speech.VERB, 0) / num_words * 10000, 1)  # relative number of verbs in text file per 10k words
        rel_freq_adj = round(num_tokens.get(spacy.parts_of_speech.ADJ, 0) / num_words * 10000, 1)  # relative number of adjectives in text file per 10k words
        rel_freq_adv = round(num_tokens.get(spacy.parts_of_speech.ADV, 0) / num_words * 10000, 1)  # relative number of adverbs in text file per 10k words

        # using the entity recogniser from Spacy to identify unique tokens (or span of tokens), which is used to identify the number of unique entities for persons, locations and organisations
        unique_entities = set([(ent.text, ent.label_) for ent in doc.ents])  # creating the set of entities for that text
        unique_entities = process_entities(unique_entities)  # doing postprocessing, which removes all symbols and lowercases the text, so that e.g. "Aarhus" and "aarhus" do not figure as unique entities (even if they are the same)

        # counting the number of unique entities in the text for persons, locations and organizations
        unique_per = sum(1 for ent in unique_entities if ent[1] == "PERSON")
        unique_loc = sum(1 for ent in unique_entities if ent[1] == "LOC")
        unique_org = sum(1 for ent in unique_entities if ent[1] == "ORG")

        # append the metrics to the list
        metrics.append([f"file{i}.txt", rel_freq_noun, rel_freq_verb, rel_freq_adj, rel_freq_adv, unique_per, unique_loc, unique_org])

    # Convert metrics list to df
    columns = ["Filename", "RelFreq NOUN", "RelFreq VERB", "RelFreq ADJ", "RelFreq ADV", "Unique PER", "Unique LOC", "Unique ORG"]
    return pd.DataFrame(metrics, columns=columns)

def start_tracker():
    """
    Start tracking the emission of the assignment
    """
    tracker = EmissionsTracker()  # setting up the tracker
    tracker.start()  # starting the tracking
    return tracker

def stop_and_save_tracker(tracker, output_folder):
    """
    Stop tracking the emission of the assignment and save it
    """
    emissions = tracker.stop()
    output_path = os.path.join(output_folder, "emissions_assignment1.csv")

    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Script", "Emissions (kg CO2eq)"]) # even though it is only one script here, I want to keep the approach consistent between the scripts
        writer.writerow(["nlp_analysis.py", emissions]) # makes rows with script name and emission (doesnt really make sense to do it like this but again I want to keep it consistent between the scripts)
