#5.# CWE-916: Use of Password Hash with Insufficient Computational Effort
# Vulnerable line: password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hexdigest()
# Description: Although PBKDF2 is a strong hashing algorithm, the number of iterations used here is insufficient. A higher number of iterations should be used to make it more secure.

import hashlib

password = input("Enter password: ")
salt = b'salt'
password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hexdigest()
print("Password hash:", password_hash)