#5.# Example 5:


import json

data = input("Enter some JSON data: ")
json.loads(data)


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is json.loads(data) which parses JSON data specified by user input without proper validation or sanitization.