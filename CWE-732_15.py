#6.# Example 6:

import json
password = input("Enter your password: ")
data = {"password": password}
json_data = json.dumps(data)
file = open("data.json", "w")
file.write(json_data) # CWE-732: Insecure Storage of Credentials
file.close()