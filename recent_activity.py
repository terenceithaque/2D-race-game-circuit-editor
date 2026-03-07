"""This script handles JSON files containing the recent user activity."""
import sys
import json
import os

def save_recent_activity(activity:dict) -> None:
    """Saves the recent user activity (usually a dictionnary) as a JSON file called 'recent_activity.json'.
    This function uses sys._MEIPASS to ensure compatibility with PyInstaller environments."""

    if getattr(sys, "_MEIPASS", False):
        # Use sys._MEIPASS if the application is running inside a PyInstaller environment
        file_path = os.path.abspath(os.path.join(sys._MEIPASS, "recent_activity.json"))

    else:
        script_dir = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(script_dir, "recent_activity.json"))


    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(activity, f, indent=4) # Save the activity


def open_recent_activity() -> dict:
    """Opens the 'recent_activity.json' file and returns the recent user activity as a dictionnary.
    In case of error, an empty dictionnary is returned."""

    try:

        if getattr(sys, "_MEIPASS", False):
            # Use sys._MEIPASS if the application is running inside a PyInstaller environment
            file_path = os.path.abspath(os.path.join(sys._MEIPASS, "recent_activity.json"))

        else:
            script_dir = os.path.dirname(__file__)
            file_path = os.path.abspath(os.path.join(script_dir, "recent_activity.json"))

        with open(file_path, "r", encoding="utf-8") as f:
            recent_activity = json.load(f)
            return recent_activity

    except Exception as e:
        #  Return an empty dictionnary in case of any error
        print(e)
        return {}           