# Assignment 1 - Extracting linguistic features using spaCy

## Repository overview
This repository contains Python scripts to extract and analyse linguistic features from the Uppsala Student English Corpus. The analysis focuses on calculating the relative frequencies of different parts of speech (POS) and the number of unique entities in each text.

### Assignment objective
The objective of this task is to extract linguistic information from a corpus of texts using spaCy. The specific steps involved are:
1. Loop over each text file in the folder called `in`
2. Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjectives, and Adverbs per 10,000 words
    - Total number of unique PER, LOC, ORGS
3. Save a table for each sub-folder (a1, a2, a3, ...) showing the extracted information.

## Data source
The corpus used is the Uppsala Student English Corpus (USE), which consists of 1489 essays written by 440 Swedish university students of English. Download the dataset from [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457?show=full) and place the files in the `in/USEcorpus` folder.

More documentation on the corpus can be found in the [`in`](https://github.com/BayesianBoi/cds-language/blob/main/assignments/assignment%201/in/USEcorpus_description.md) folder.

## Steps for running the analysis

### Setting up the environment
1. **Set up the virtual environment and install requirements:**
    ```bash
    bash setup.sh
    ```
2. **Activate the virtual environment:**
    ```bash
    source EnvLang1/bin/activate
    ```

### Running the analysis
1. **[Download](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457?show=full) and place the dataset in the `in/USEcorpus` folder**

2. **Run the script:**
    ```bash
    python src/nlp_analysis.py
    ```
## Summary of results

### Example table of data 
The `out` folder contains analysed CSV files for all of the subfolders. Below is an example table showing the extracted linguistic features for subfolder `c1`:

| Filename | RelFreq NOUN | RelFreq VERB | RelFreq ADJ | RelFreq ADV | Unique PER | Unique LOC | Unique ORG |
|----------|---------------|--------------|-------------|-------------|------------|------------|------------|
| file1.txt | 1573.6 | 933.6 | 472.9 | 403.6 | 38 | 0 | 5 |
| file2.txt | 1742.5 | 816.4 | 580.8 | 284.3 | 27 | 0 | 3 |
| file3.txt | 1177.7 | 1021.6 | 649.2 | 508.3 | 17 | 0 | 8 |
| file4.txt | 1379.3 | 974.8 | 563.7 | 484.1 | 26 | 0 | 6 |
| file5.txt | 1092.9 | 1163.2 | 398.1 | 288.8 | 18 | 0 | 3 |
| file6.txt | 1231.9 | 1025.5 | 461.1 | 426.7 | 14 | 0 | 5 |
| file7.txt | 1321.8 | 1219.7 | 434.2 | 408.7 | 15 | 0 | 5 |

### Example usage of the analysed data
The corpus contains essays where students were explicitly asked to write in different styles: personal, formal, and academic. The extracted linguistic features can be used to compare the relative usage of parts of speech between these styles.

- **Personal style**: Includes subfolders `a1` and `a3`.
- **Formal style**: Includes subfolders `a2`, `a4`, and `b1`.
- **Academic style**: Includes subfolders `b4` and `b5`.

#### Plots of POS tag frequencies
The following plots show the comparison of part-of-speech tag frequencies between personal, formal and academic styles:

Relative frequency of nouns | Relative frequency of verbs 
:-------------------------:|:-------------------------:
![](https://github.com/BayesianBoi/cds-language/blob/main/assignments/assignment%201/out/RelFreq%20NOUN_comparison.png) |  ![](https://github.com/BayesianBoi/cds-language/blob/main/assignments/assignment%201/out/RelFreq%20VERB_comparison.png)

Relative frequency of adjectives | Relative frequency of adverbs
:-------------------------:|:-------------------------:
![](https://github.com/BayesianBoi/cds-language/blob/main/assignments/assignment%201/out/RelFreq%20ADJ_comparison.png) |  ![](https://github.com/BayesianBoi/cds-language/blob/main/assignments/assignment%201/out/RelFreq%20ADV_comparison.png)

*Please note that these plots are purely descriptive and no statistical analysis has been conducted. They are simply an example use-case of the extracted linguistic features.*


### Carbon Emissions Tracking
We used CodeCarbon to track the carbon-emissions caused by running this analysis. The CSV detailing the emissions can be found in the `out` folder. The detailed results of the emissions will be discussed in Assignment 5.

## Limitations and possible improvements

### Limitations
- The analysis uses uniform text processing without considering specific nuances of each sub-folder's content. The description for the b3-subfolder says that "..Essays may still contain words in other languages than English, or from earlier periods of English, items quoted directly from dictionaries, and lists of references.".
  Therefore, using the same "tool" for all of the processing without considering whether the data is even in the same language might be suboptimal.

### Possible improvements
- Implement more advanced NLP techniques to detect more subtle linguistic features. However, it really depends on what kind of analysis one were to use the data for.
