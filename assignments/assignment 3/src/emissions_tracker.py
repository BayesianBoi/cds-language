import os
import csv
from codecarbon import EmissionsTracker
"""
Script for measuring the emission of running the other script
"""

def start_tracker():
    """
    Start tracking the emission of the script
    """
    tracker = EmissionsTracker(log_level='error')  # setting up the tracker and disable logging messages
    tracker.start() # starting the tracking
    return tracker

def stop_and_save_tracker(tracker, script_name):
    """
    Start tracking the emission of the script and add it to CSV 
    """
    emissions = tracker.stop() #stop the tracker
    output_folder = "out"
    output_path = os.path.join(output_folder, "emissions_assignment3.csv")
    file_exists = os.path.isfile(output_path) # checks if the csv already exists
    
    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file) # write object so that we can append the emissio n for that script
        if not file_exists: # if the csv file does not already exist it will create new rows for it with the name of the script and the emissions
            writer.writerow(["Script", "Emissions (kg CO2)"]) 
        writer.writerow([script_name, emissions]) # append the current script and its emissions to the csv
