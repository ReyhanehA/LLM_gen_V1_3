#2.# CWE-916: Use of Password Hash with Insufficient Computational Effort
# Vulnerable line: password_hash = hashlib.sha1(password.encode()).hexdigest()
# Description: The SHA-1 hashing algorithm used here is not secure enough for password storage as it can be easily cracked with modern computing power.

import hashlib

password = input("Enter password: ")
password_hash = hashlib.sha1(password.encode()).hexdigest()
print("Password hash:", password_hash)