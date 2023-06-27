#9.# Example 9:

import json
data = {'username': 'admin', 'password': 'password123'}
json_data = json.dumps(data)
print(json_data) # CWE-732: Insecure Storage of Credentials