#3.# Example 3:

import requests

url = input("Enter a URL: ")
response = requests.get(url)
if response.status_code == 200:
    print("Page loaded successfully.")
else:
    print("Error loading page.")

# The vulnerable line is line 3, where user input is being directly passed to the requests.get() function without any validation, which can lead to server-side request forgery attacks.