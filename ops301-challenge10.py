#!/usr/bin/env python3
#Script: Ops 301 Class 10 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/24/2023
# Assistance from Chat GPT

# Main

# create a new file with open()
with open('wiseman_file.txt', 'w') as f:
    # append three lines to the file
    f.write('First line\n')
    f.write('Second line\n')
    f.write('Third line\n')

# read the first line of the file and print it to the screen
with open('wiseman_file.txt', 'r') as f:
    first_line = f.readline()
    print(first_line)

# delete the file using os.remove()
import os
os.remove('wiseman_file.txt')

# Done