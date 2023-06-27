#9.# Example 9:


import requests

url = input("Enter a URL: ")
response = requests.get(url, verify=False)
print(response.content)


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is response = requests.get(url, verify=False) which sends a request to a URL specified by user input without proper validation or sanitization.