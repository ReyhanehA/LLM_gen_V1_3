#2.# CWE-614: Sensitive Data in URL

import requests

username = 'admin'
password = 'password'

response = requests.get('https://example.com/login?username={}&password={}'.format(username, password))

# The vulnerable line is response = requests.get('https://example.com/login?username={}&password={}'.format(username, password))
# This code sends sensitive data (username and password) in the URL, which can be intercepted and viewed by attackers.