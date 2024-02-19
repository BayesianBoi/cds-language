# Extracting linguistic features using spaCy

This assignment concerns using ```spaCy``` to extract linguistic information from a corpus of texts.

The corpus is an interesting one: *The Uppsala Student English Corpus (USE)*. All of the data is included in the folder called ```in``` but you can access more documentation via [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

## Objective of the analysis
The objective of this NLP-analysis is to compare the complexity of written English for different grades in the Swedish highschool system. The complexity of their language is rated on the number of nouns, verbs, adjectives, adverbs, and the unique number of persons, locations and organizations. See README in "/in" for specifics about the corpus.

## Steps of the analysis

For this assignment, we are doing the following:
1. Loading the necessary text files from the large corpus
2. For each of the folders containing text, we are extracting various NLP information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
3. Saving the NLP metrics for each of the subfolder in the following format:

    |Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
    |---|---|---|---|---|---|---|---|
    |file1.txt|---|---|---|---|---|---|---|
    |file2.txt|---|---|---|---|---|---|---|
    |etc|---|---|---|---|---|---|---|

3.1. The metrics are then saved in a CSV file containing all of the metrics for each individual subfolder (the csv-file is named after the subfolder). These CSV-files are saved in the "out"-folder