#!/bin/bash
#Script: Ops 301 Class 03 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/15/2023
# Assistance from Chat GPT

# Main 

# Prompt user for Path
read -p "Enter the directory path: " dir_path

# Prompt user for permission number
read -p :Enter the permissions number: " perms_number

# Navigate to the directory
cd $dir_path

# Change permissions of all files in the directory
chmod -R $perm_number *

# Print directory contents and new permissions settings 
echo "Directory contents:"
ls -l

# End