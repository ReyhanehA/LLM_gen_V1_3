#8.# Example 8:

import hashlib
password = input("Enter your password: ")
hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
file = open("password.txt", "w")
file.write(hashed_password) # CWE-732: Insecure Storage of Credentials
file.close()