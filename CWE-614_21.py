#2.# CWE-614: Sensitive Data in URL

import requests

username = 'admin'
password = 'password'
url = 'https://example.com/login?username=' + username + '&password=' + password
response = requests.get(url)
print(response.text)

# The vulnerable line is url = 'https://example.com/login?username=' + username + '&password=' + password, as it includes sensitive data in the URL.