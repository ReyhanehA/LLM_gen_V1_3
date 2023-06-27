#3.# CWE-798: Use of Hard-coded URLs
# Vulnerable line: url = "http://example.com/api"
# Description: The URL is hard-coded in the code, making it difficult to change and potentially exposing sensitive information.

import requests

url = "http://example.com/api"
response = requests.get(url)
data = response.json()