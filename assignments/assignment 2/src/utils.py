import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

"""
Helper functions for the the nn and lr script
"""

def load_data(model_folder):
    """
    Loads the vectorized data and labels
    """
    X_transformed, y = joblib.load(os.path.join(model_folder, "vectorized_data.pkl"))
    return X_transformed, y

def save_model(model, model_folder, model_name):
    """
    Saves the trained model
    """
    joblib.dump(model, os.path.join(model_folder, model_name))

def save_report(report, output_folder, report_name):
    """
    Saves the report
    """
    with open(os.path.join(output_folder, report_name), "w") as f:
        f.write(report)

def plot_confusion_matrix(cm, classes, title="Confusion matrix", output_path=None):
    """
    Plots a confusion matrix
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Greens", xticklabels=classes, yticklabels=classes)
    plt.title(title)
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.savefig(output_path)
    plt.show()
