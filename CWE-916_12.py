#3.# CWE-916: Use of Password Hash with Insufficient Computational Effort
# Vulnerable line: password_hash = hashlib.sha256(password.encode()).hexdigest()
# Description: Although SHA-256 is a strong hashing algorithm, it is still vulnerable to brute force attacks. A more secure algorithm like bcrypt or scrypt should be used.

import hashlib

password = input("Enter password: ")
password_hash = hashlib.sha256(password.encode()).hexdigest()
print("Password hash:", password_hash)