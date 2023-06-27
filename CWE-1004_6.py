#7.# CWE-1004: Unintended Execution of Code
# Vulnerable line: json.loads(user_input)
import json
user_input = input("Enter a JSON string: ")
data = json.loads(user_input)
print(data)