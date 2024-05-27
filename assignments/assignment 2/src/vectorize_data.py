import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os
from emission_tracker import start_tracker, stop_and_save_tracker

def load_data(main_file):
    """
    Load the fake news dataset
    """
    df = pd.read_csv(main_file)
    X = df["text"]
    y = df["label"]
    return X, y

def vectorize_data(X):
    """
    Vectorize the data using Tf-idf
    """
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True, max_df=0.95, min_df=0.05, max_features=100) # removes the most common words and the most rare words and only keep top 100 features
    X_transformed = vectorizer.fit_transform(X) # fit the vectorizer
    return X_transformed, vectorizer

def save_data(X_transformed, y, model_output_folder):
    """
    Save the vectorized data and labels
    """
    joblib.dump((X_transformed, y), os.path.join(model_output_folder, "vectorized_data.pkl"))

def save_vectorizer(vectorizer, model_output_folder):
    """
    Save the vectorizer
    """
    joblib.dump(vectorizer, os.path.join(model_output_folder, "vectorizer.pkl"))

def main():
    main_file = "in/fake_or_real_news.csv"
    model_output_folder = "models/"
    output_folder = "out/"
    
    tracker = start_tracker() # start tracking the emissions
    
    # load the dataset
    X, y = load_data(main_file)
    
    # vectorize the text data
    X_transformed, vectorizer = vectorize_data(X)
    
    # save the vectorized data and labels
    save_data(X_transformed, y, model_output_folder)
    
    # save the vectorizer
    save_vectorizer(vectorizer, model_output_folder)
    
    # stop tracking emissions and save it
    stop_and_save_tracker(tracker, output_folder, "vectorize_data.py")

if __name__ == "__main__":
    main()
