#10.# Example 10:


import json

data = input("Enter some JSON data: ")
json.loads(data, strict=False)


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is json.loads(data, strict=False) which parses JSON data specified by user input without proper validation or sanitization.