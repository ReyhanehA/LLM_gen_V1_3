#8.# Example 8:

import requests
password = input("Enter your password: ")
response = requests.post('https://example.com/login', data={'username': 'admin', 'password': password}) # CWE-732: Insecure Storage of Credentials