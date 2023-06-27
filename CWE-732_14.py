#5.# Example 5:

import requests
password = input("Enter your password: ")
requests.post("http://example.com/login", data={"password": password}) # CWE-732: Insecure Storage of Credentials