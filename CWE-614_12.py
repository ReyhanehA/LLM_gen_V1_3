#3.# CWE-614: Plaintext Storage of a Password

import hashlib

password = 'password123'
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# The vulnerable line is password = 'password123'
# This code stores a plaintext password, which can be easily accessed by attackers if the system is compromised.