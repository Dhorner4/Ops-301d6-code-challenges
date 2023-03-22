#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables
def print_directory_contents(path):
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
    for file in files:
        print(f"File: {os.path.join(root, file)}")
# Main
if __name__ == "__main__":
    # Read user input here into a variable
    path = input("Enter the directory path: ")

    # Call the function with the user input path
    print_directory_contents(path)

# End
