#10.# Example 10: CWE-798 - Use of Unvalidated Input in JSON Parsing

import json

json_string = input("Enter the JSON string: ")
data = json.loads(json_string) # vulnerable line
print(data['name'])