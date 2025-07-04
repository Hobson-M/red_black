# Import tkinter to create the widgets and windows, as well as the os and sys files inorder to integrate with the base OS
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font
import os
import sys


# Create a variable to record history
HISTORY_FILE = "roulette_history_gui.tx"

# Setting the default threshold number, which is 0 from which the countdown will begin when miss streaks start appearing. ZERO means the alert is off.

DEFAULT_THRESHOLD = 0

# Set the blinking speeds for alerts in millisecond (500 ms = half a second).

BLINK_INTERVAL_MS = 500

# Define a variable for all red numbers in the European roulette

RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

# Define a variable for all black numbers in the European roulette

BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

# Define the zero number, green number
GREEN_NUMBER = 0

# Define the main application class, which inherits from tk.Tk.
# Inheriting from tk.Tk makes this class the main window of our application.

def determine_colors(number):
 # Determines the color ('red', 'black', or 'green') for a given roulette number
    if number == GREEN_NUMBER: return "green"
    if number in RED_NUMBERS: return "red"
    if number in BLACK_NUMBERS: return "black"
    return "invalid"

# Create a function for loading past spin history from the text file when the application starts

def rb_load_history():
  
    # Initialize an empty list to store the history.
    history = []
    # Check if the history file actually exists in the current directory.
    if os.path.exists(HISTORY_FILE):
        try:
            # Open the file in read mode ('r').
            with open(HISTORY_FILE, 'r') as f:
                # Read each line, strip leading/trailing whitespace, convert to lowercase, and add it to the history list.
                # It also filters to ensure only valid colors are loaded, adding robustness.
                history = [line.strip().lower() for line in f if line.strip().lower() in ["red", "black", "green"]]
        except IOError as e:
            # If there's an error reading the file (e.g., permissions issue), show an error message.
            messagebox.showerror("History Load Error", f"Could not load history: {e}")
    # Return the loaded history list (will be empty if the file didn't exist or an error occurred).
    return history