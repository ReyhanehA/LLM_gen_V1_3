#1.# CWE-916: Use of Password Hash with Insufficient Computational Effort
# Vulnerable line: password_hash = hashlib.md5(password.encode()).hexdigest()
# Description: The MD5 hashing algorithm used here is vulnerable to brute force attacks and can be easily cracked. A stronger hashing algorithm should be used.

import hashlib

password = input("Enter password: ")
password_hash = hashlib.md5(password.encode()).hexdigest()
print("Password hash:", password_hash)