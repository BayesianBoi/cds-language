import joblib
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
import os
from emission_tracker import start_tracker, stop_and_save_tracker
from utils import load_data, save_model, save_report, plot_confusion_matrix

"""
Script for running neural network classifier 
"""

def train_neural_network(X_train, y_train):
    """
    Train the neural network model
    """
    classifier = MLPClassifier(activation="relu", hidden_layer_sizes=(20,), max_iter=1000, random_state=420)
    classifier.fit(X_train, y_train)
    return classifier

def main():
    models_folder = "models/"
    output_folder = "out/"
    
    tracker = start_tracker()  # start tracking the emissions
    
    X_transformed, y = load_data(models_folder) # load the vectorized data
    
    # split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=69)
    
    # Train the neural network model
    classifier = train_neural_network(X_train, y_train)
    
    # make predictions
    y_pred = classifier.predict(X_test)
    
    # make the report
    report = classification_report(y_test, y_pred, target_names=["FAKE", "REAL"])
    print(report)
    
    # save the report
    save_report(report, output_folder, "NN_report.txt")
    
    # save the model
    save_model(classifier, models_folder, "NN_model.pkl")
    
    # plot a confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plot_confusion_matrix(cm, classes=["FAKE", "REAL"], title="CM - Neural Network", output_path=os.path.join(output_folder, "CM_NN.png"))
    
    # stop tracking emissions and save it
    stop_and_save_tracker(tracker, output_folder, "neural_network.py")

if __name__ == "__main__":
    main()
