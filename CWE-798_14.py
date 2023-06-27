#5.# CWE-798: Use of Hard-coded API Keys
# Vulnerable line: api_key = "myapikey123"
# Description: The API key is hard-coded in the code, making it easily accessible to attackers.

import requests

api_key = "myapikey123"
url = f"http://example.com/api?key={api_key}"
response = requests.get(url)
data = response.json()