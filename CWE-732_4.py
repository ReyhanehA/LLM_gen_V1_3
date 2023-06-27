#5.# Example 5:

import hashlib
password = input("Enter your password: ")
hash_object = hashlib.sha256(password.encode())
print(hash_object.hexdigest()) # CWE-732: Insecure Storage of Credentials