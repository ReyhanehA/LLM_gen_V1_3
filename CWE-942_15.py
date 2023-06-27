#6.# Example 6:


import json

json_string = input("Enter a JSON string: ")
data = json.loads(json_string)

print(data)


# CWE-942: Improper Neutralization of Special Elements used in a JSON String ('JSON Injection')
# The vulnerable line is line 2, where user input is directly used to construct a JSON string without proper sanitization or validation.