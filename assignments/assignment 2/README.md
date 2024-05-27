# Assignment 2 - Text classification benchmarks

## Repository overview
This repository contains Python scripts to train and evaluate binary classification models on text data using the Fake News Dataset. The models used are logistic Regression and a neural Network. The analysis focuses on measuring the performance of these models.

### Assignment objective
The objective of this task is to classify whether the news is fake or real. The specific steps involved are:
1. Train simple benchmark machine learning classifiers on structured text data
2. Produce understandable outputs and trained models which can be reused
3. Save those results in a clear way which can be shared or used for future analysis

## Data source
The dataset used is the Fake News Dataset, which should be placed in the `in` folder. Ensure the file is named `fake_or_real_news.csv`.

## Steps for running the analysis

### Setting up the environment
1. **Set up the virtual environment and install requirements:**
    ```bash
    bash setup.sh
    ```
2. **Activate the virtual environment:**
    ```bash
    source EnvLang2/bin/activate
    ```

### Running the analysis
Important that you vectorize the data before proceding with the models
1. **Vectorize the data:**
    ```bash
    python src/vectorize_data.py
    ```
- **Running the logistic regression:**
    ```bash
    python src/logistic_regression.py
    ```
- **Running the neural network:**
    ```bash
    python src/neural_network.py
    ```


### Summary of the results
The `out` folder contains the classification report for both of the classification methods. Below are the reports for both of the models:

#### Logistic Regression:
| Label       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| FAKE        | 0.82      | 0.80   | 0.81     | 635     |
| REAL        | 0.80      | 0.83   | 0.82     | 632     |
| **Accuracy**   | **0.81**   |        |          | 1267   |
| **Macro Avg**  | 0.81      | 0.81   | 0.81     | 1267   |
| **Weighted Avg** | 0.81      | 0.81   | 0.81     | 1267   |

#### Neural Network
| Label       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| FAKE        | 0.82      | 0.81   | 0.81     | 635     |
| REAL        | 0.81      | 0.82   | 0.81     | 632     |
| **Accuracy**   | **0.81**   |        |          | 1267   |
| **Macro Avg**  | 0.81      | 0.81   | 0.81     | 1267   |
| **Weighted Avg** | 0.81      | 0.81   | 0.81     | 1267   |

### Plots of confusion matrices
The following plots show the confusion matrices for both models:

#### Logistic Regression
![Confusion Matrix for Logistic Regression](https://github.com/BayesianBoi/cds-language/blob/main/assignments/assignment%202/out/CM_LR.png)

#### Neural Network
![Confusion Matrix for Neural Network](https://github.com/BayesianBoi/cds-language/blob/main/assignments/assignment%202/out/CM_NN.png)


## Carbon emissions tracking
We used CodeCarbon to track the carbon-emissions caused by running this analysis. The CSV detailing the emissions can be found in the `out` folder. The detailed results of the emissions will be discussed in Assignment 5.

## Limitations and possible improvements
Both of the models achieved almost exactly the same accuracy in classifying the fake news dataset. However, there are several limitations and areas for potential improvements.
### Limitations
- **Model simplicity:** Both models are relatively simple. They may not capture complex patterns in the data as effectively as more advanced models

### Possible improvements
- **GridSearch:** We did not optimise the hyperparameters and just went with a basic approach. Further tuning the model might have yielded higher accuracy
- **More advanced models:** Implementing more advanced classification approaches such as BERT or Google's T5-Flan could improve the accuracy
