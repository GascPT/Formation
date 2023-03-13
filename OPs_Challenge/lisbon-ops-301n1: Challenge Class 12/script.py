#!/bin/python
import requests

# Prompt the user to enter a URL
url = input("Enter the destination URL: ")

# Prompt the user to select a HTTP method
http_method = input("Select a HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the request details and ask the user to confirm
print("Request details:")
print(f"URL: {url}")
print(f"HTTP method: {http_method}")
confirm = input("Confirm the request (y/n): ")

if confirm.lower() != 'y':
    print("Request canceled.")
    exit()

# Send the request using requests library
response = requests.request(http_method.upper(), url)

# Print the response header information
print("Response header information:")
for key, value in response.headers.items():
    # Translate HTTP status codes to plain terms
    if key.lower() == 'status':
        if value.startswith('404'):
            value = 'Site not found'
        elif value.startswith('500'):
            value = 'Internal server error'
        # Add more translations as needed
    print(f"{key}: {value}")