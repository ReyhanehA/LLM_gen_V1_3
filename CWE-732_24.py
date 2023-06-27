#5.# Example 5:

import requests

url = input("Enter a URL: ") # CWE-732: Incorrect Permission Assignment for Critical Resource
response = requests.get(url)

if response.status_code == 200:
    print(response.content)
else:
    print("Error:", response.status_code)

# The vulnerable line is the input() function, which allows any user to enter a URL without proper authentication or authorization.