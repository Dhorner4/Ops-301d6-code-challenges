#!/bin/bash
#Script: Ops 301 Class 04 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/16/2023
# Assistance from Chat GPT


# Define the menu options
options=("Hello world" "Ping self" "IP info" "Exit")

# Define the function for the Hello world option
function hello_world {
    echo "Hello world!"
}

# Define the function for the Ping self option
function ping_self {
    ping -c 4 127.0.0.1
}

# Define the function for the IP info option
function ip_info {
    ifconfig
}

# Loop to display the menu and execute the selected option
while true; do
    # Display the menu
    echo "Select an option:"
    for i in "${!options[@]}"; do
        echo "$i. ${options[$i]}"
    done

    # Read the user's input
    read -p "Enter option number: " option

    # Evaluate the user's input and execute the corresponding option
    case "$option" in
        0) hello_world ;;
        1) ping_self ;;
        2) ip_info ;;
        3) exit ;;
        *) echo "Invalid selection" ;;
    esac
done