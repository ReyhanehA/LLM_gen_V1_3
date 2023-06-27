#4.# CWE-614: Use of Hard-coded Credentials

import requests

username = 'admin'
password = 'password'

response = requests.post('https://example.com/login', data={'username': username, 'password': password})

# The vulnerable line is username = 'admin' and password = 'password'
# This code uses hard-coded credentials, which can be easily discovered by attackers and used to gain unauthorized access.