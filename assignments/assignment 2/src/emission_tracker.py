import os
import csv
from codecarbon import EmissionsTracker
"""
Script for measuring the emission of running the other scripts in this assignment
"""

def start_tracker():
    """
    Start tracking the emission of the script
    """
    tracker = EmissionsTracker() # setting up the tracker
    tracker.start() # starting the tracking
    return tracker

def stop_and_save_tracker(tracker, output_folder, script_name):
    """
    Start tracking the emission of the script and append it to CSV (So that there's seperate entries for the three scripts)
    """
    emissions = tracker.stop() #stop the tracker
    output_path = os.path.join(output_folder, "emissions_assignment2.csv") 
    
    file_exists = os.path.isfile(output_path) # checks if the csv already exists
    
    with open(output_path, mode="a", newline="") as file:
        writer = csv.writer(file) # write object so that we can append the emissio n for that script
        if not file_exists: # if the csv file does not already exist it will create new rows for it with the name of the script and the emissions
            writer.writerow(["Script", "Emissions (kg CO2)"]) 
        writer.writerow([script_name, emissions]) # append the current script and its emissions to the csv
