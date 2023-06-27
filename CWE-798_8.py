#9.# CWE-798: Improper Validation of JSON Input
# Vulnerable line: data = json.loads(json_string)
# Description: The code does not validate if the JSON input is safe.

import json

json_string = input('Enter JSON: ')
data = json.loads(json_string)
print(data)