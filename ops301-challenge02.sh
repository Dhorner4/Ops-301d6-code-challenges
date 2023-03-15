#!/bin/bash

#Script: Ops 301 Class 02 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/14/2023
# With assistance from ChatGPT

# Main 
# Timestamped echo statements
echo "Copying /var/log/syslog to current directory..."
echo "Current date and time will be appended to the filename."

# Get current date and time
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

# Copy syslog to current directory with timestamped filename
cp /var/log/syslog ./syslog_$timestamp

# Timestamped echo statement
echo "Done. Copied file: syslog_$timestamp"


# End