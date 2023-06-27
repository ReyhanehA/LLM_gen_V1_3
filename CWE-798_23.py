#4.# Example 4:


import requests

url = input("Enter a URL: ")
response = requests.get(url)
print(response.content)


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is response = requests.get(url) which sends a request to a URL specified by user input without proper validation or sanitization.