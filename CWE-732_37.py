#9.# Example 9:

import urllib.request

url = input("Enter a URL: ")
response = urllib.request.urlopen(url)

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 3, where the user input is being used to make an HTTP request without proper validation. This can lead to arbitrary code execution and compromise of the system.