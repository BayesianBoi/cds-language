import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import os
from emission_tracker import start_tracker, stop_and_save_tracker
from utils import load_data, save_model, save_report, plot_confusion_matrix

"""
Script for running logistic regression classifier
"""

def train_logistic_regression(X_train, y_train):
    """
    Train the logistic regression model
    """
    log_reg = LogisticRegression()
    log_reg.fit(X_train, y_train)
    return log_reg

def main():
    models_folder = "models/"
    output_folder = "out/"
    
    tracker = start_tracker()     # start tracking the emissions
    
    X_transformed, y = load_data(models_folder) # load the vectorized data
    
    # split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=69)
    
    # train the lr model
    log_reg = train_logistic_regression(X_train, y_train)
    
    # make predictions
    y_pred = log_reg.predict(X_test)
    
    # make the report
    report = classification_report(y_test, y_pred, target_names=["FAKE", "REAL"])
    print(report)
    
    # save the report
    save_report(report, output_folder, "LR_report.txt")
    
    # save the model
    save_model(log_reg, models_folder, "LR_model.pkl")
    
    # plot a confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plot_confusion_matrix(cm, classes=["FAKE", "REAL"], title="CM - Logistic Regression", output_path=os.path.join(output_folder, "CM_LR.png"))
    
    # stop tracking emissions and save it
    stop_and_save_tracker(tracker, output_folder, "logistic_regression.py")

if __name__ == "__main__":
    main()
