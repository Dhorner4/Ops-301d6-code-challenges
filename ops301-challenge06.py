#!/usr/bin/env python3
#Script: Ops 301 Class 06 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/20/2023
# Assistance from Chat GPT

# How to use Linux/Bash commands within Python
# First import the os library
import os

# Execute bash commands using os.system and store the output in variables
whoami_output = os.popen('whoami').read()
ip_output = os.popen('ip a').read()
lshw_output = os.popen('lshw -short').read()

# Print the output of the bash commands using print() function
print("The output of 'whoami' command is:")
print(whoami_output)

print("The output of 'ip a' command is:")
print(ip_output)

print("The output of 'lshw -short' command is:")
print(lshw_output)


