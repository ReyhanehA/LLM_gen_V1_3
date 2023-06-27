#6.# Example 6:

import base64
password = input("Enter your password: ")
encoded_password = base64.b64encode(password.encode())
print(encoded_password) # CWE-732: Insecure Storage of Credentials