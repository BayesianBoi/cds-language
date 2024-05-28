# Assignment 3 - Query expansion with word embeddings

## Repository overview
This repository contains Python scripts for analyzing song lyrics from a dataset of 57,650 English-language songs. The analysis focuses on finding the most common themes in the lyrics of specific artists using query expansion with word embeddings

### Assignment objective
The objective of this assignment is to:
1. Load the song lyric data
2. Load a word embedding model via `gensim`
3. Take a given word as an input and finds the most similar words via word embeddings
4. Find how many songs for a given artist feature terms from the expanded query
5. Calculate the percentage of that artist's songs featuring those terms
6. Print and/or save results in an easy-to-understand way

## Data source
The dataset used is the Spotify Songs Dataset, which should be placed in the `in` folder. Ensure the file is named `spotify-songs.csv`. The dataset can be found [here](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs)

## Steps for running the analysis

### Setting up the environment
1. **Set up the virtual environment and install requirements:**
    ```bash
    bash setup.sh
    ```
2. **Activate the virtual environment:**
    ```bash
    source EnvLang3/bin/activate
    ```

**Important:** Ensure `scipy==1.12.0` is installed before `gensim` as the latest version of `scipy` removed a function that `gensim` depends on. The provided `requirements.txt` and `setup.sh` take care of this

### Running the analysis
1. **Run the main analysis script:**
    ```bash
    python src/main.py <artist> <keyword> <--top_words TOP_WORDS> <--show_similarity>
    ```

### Arguments
- `<artist>`: Name of the artist (e.g., `ABBA`)
- `<keyword>`: Keyword for the lyrics search (e.g., `dance`)
- `<--top_words>`: Is optional: Number of similar words to retrieve (default is 10)
- `<--show_similarity>`: Is optional: Include this flag to disable similarity scores for similar words

### Example run
```bash
python src/main.py abba dance --top_words 10 --show_similarity
```

### Summary of the results
The `out` folder contains a CSV file that have logged some example runs. Below are the result:

| Artist                  | Keyword      | Top_words | Similar_Words                                                                                                                                                              | Matching_Songs | Total_Songs | Percentage     |
|-------------------------|--------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------|----------------|
| abba                    | love         | 10        | ['loves (0.64)', 'passion (0.63)', 'loved (0.60)', 'romantic (0.59)', 'lovers (0.59)', 'lover (0.58)', 'you (0.58)', 'me (0.58)', 'affection (0.58)', 'always (0.57)']    | 113            | 113         | 100            |
| miley cyrus             | construction | 10        | ['building (0.67)', 'projects (0.64)', 'project (0.60)', 'constructed (0.60)', 'built (0.59)', 'constructing (0.58)', 'build (0.58)', 'renovation (0.57)', 'infrastructure (0.57)', 'industrial (0.54)'] | 5              | 147         | 3.401360544    |
| the beatles             | city         | 10        | ['cities (0.71)', 'town (0.64)', 'downtown (0.63)', 'mayor (0.58)', 'area (0.54)', 'residents (0.54)', 'towns (0.53)', 'where (0.53)', 'capital (0.53)', 'municipal (0.51)'] | 37             | 178         | 20.78651685    |
| red hot chili peppers   | california   | 10        | ['calif. (0.71)', 'angeles (0.62)', 'san (0.60)', 'oregon (0.60)', 'diego (0.58)', 'texas (0.58)', 'arizona (0.57)', 'los (0.56)', 'nevada (0.56)', 'francisco (0.54)']  | 53             | 173         | 30.63583815    |
| elton john              | plane        | 10        | ['airplane (0.77)', 'planes (0.74)', 'jet (0.71)', 'crashed (0.70)', 'aircraft (0.69)', 'flight (0.68)', 'airliner (0.66)', 'crash (0.66)', 'helicopter (0.63)', 'flew (0.63)'] | 7              | 175         | 4              |

### Carbon emissions tracking
We used CodeCarbon to track the carbon emissions caused by running this analysis. The CSV detailing the emissions can be found in the `out` folder

### Limitations and possible improvements
#### Limitations
- **Model simplicity**: The current model and approach are relatively simple and may not capture complex patterns in the data as effectively as more advanced models
- **Execution time**: The current setup is quite slow and is taking over a minute per search, which is not feasible for real-world applications

#### Possible improvements
- **Advanced models**: Implementing more advanced models such as BERT or Google's T5-Flan could improve the accuracy and speed of the search
- **Optimisation**: Optimise the current implementation to reduce execution time and improve efficiency. The Glove training set is a jack-of-all-trades kind of model, quite well broadly but not optimised for all
