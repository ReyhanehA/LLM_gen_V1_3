#2.# Example 2: CWE-798 - Use of Weak Cryptographic Hash

import hashlib

password = "password123"
hash_object = hashlib.md5(password.encode()) # vulnerable line
print(hash_object.hexdigest())