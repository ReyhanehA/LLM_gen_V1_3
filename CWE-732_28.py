#9.# Example 9:

import urllib.request

url = input("Enter a URL: ") # CWE-732: Incorrect Permission Assignment for Critical Resource
response = urllib.request.urlopen(url)

print(response.read().decode())

# The vulnerable line is the input() function, which allows any user to enter a URL without proper authentication or authorization.