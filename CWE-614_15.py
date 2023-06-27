#6.# CWE-614: Use of Weak Cryptographic Hash

import hashlib

password = 'password123'
hashed_password = hashlib.md5(password.encode()).hexdigest()

# The vulnerable line is hashed_password = hashlib.md5(password.encode()).hexdigest()
# This code uses a weak cryptographic hash (MD5), which can be easily cracked by attackers.