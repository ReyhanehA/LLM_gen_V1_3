#7.# Example 7:

import base64
password = input("Enter your password: ")
encoded_password = base64.b64encode(password.encode("utf-8"))
file = open("password.txt", "w")
file.write(encoded_password.decode("utf-8")) # CWE-732: Insecure Storage of Credentials
file.close()