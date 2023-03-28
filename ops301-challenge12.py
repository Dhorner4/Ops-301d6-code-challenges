#!/usr/bin/env python3
#Script: Ops 301 Class 12 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/28/2023
# Assistance from Chat GPT

# Main

import requests

# Prompt the user for the destination URL
url = input("Enter the destination URL: ")

# Prompt the user for the HTTP method
http_method = input("Select an HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the request that will be sent and ask for confirmation
print(f"Sending {http_method} request to {url}")
confirmation = input("Do you want to proceed? (y/n) ")

if confirmation.lower() == "y":
    # Send the request using the requests library
    response = requests.request(http_method, "https://www.google.com")

    # Print the response headers
    print("Response headers:")
    for header, value in response.headers.items():
        if header.lower() == "content-type":
            print(f"{header}: {value.split(';')[0]}")
        else:
            print(f"{header}: {value}")

    # Translate the response code into plain terms
    if response.status_code == 200:
        print("Request successful")
    elif response.status_code == 201:
        print("Resource created")
    elif response.status_code == 204:
        print("No content")
    elif response.status_code == 400:
        print("Bad request")
    elif response.status_code == 401:
        print("Unauthorized")
    elif response.status_code == 403:
        print("Forbidden")
    elif response.status_code == 404:
        print("Site not found")
    elif response.status_code == 405:
        print("Method not allowed")
    elif response.status_code == 500:
        print("Internal server error")
    else:
        print(f"Unknown response code: {response.status_code}")
else:
    print("Request cancelled")

    # Done