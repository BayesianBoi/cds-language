# Assignment 2 - Text classification benchmarks

This assignment is about using ```scikit-learn``` to train simple (binary) classification models on text data. For this assignment, we'll continue to use the Fake News Dataset.

For this exercise, you should write *two different notebooks*. One script should train a logistic regression classifier on the data; the second notebook should train a neural network on the same dataset. Both notebooks should do the following:

- Save the classification report to a text file the folder called ```out```
- Save the trained models and vectorizers to the folder called ```models```

## Objective

This assignment is designed to test that you can:

1. Train simple benchmark machine learning classifiers on structured text data;
2. Produce understandable outputs and trained models which can be reused;
3. Save those results in a clear way which can be shared or used for future analysis

## Some notes
- The vectorizer is in a seperate notebook, and saves the vectorized data and the vectorizer-model into the model folder.
- Both models perform similarly well- with an accuracy of .86 and .87 for the LR and NN classifiers, respectively.
