#9.# Example 9:

import hmac
password = input("Enter your password: ")
key = b"secret_key"
hashed_password = hmac.new(key, password.encode("utf-8"), hashlib.sha256).hexdigest()
file = open("password.txt", "w")
file.write(hashed_password) # CWE-732: Insecure Storage of Credentials
file.close()