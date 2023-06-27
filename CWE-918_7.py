#8.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: json.loads(json_data)
import json
json_data = input("Enter JSON data: ")
data = json.loads(json_data)
print(data)