#9.# Example 9:


import hashlib

password = input("Enter a password: ")
hash_object = hashlib.sha256(password.encode())

print(hash_object.hexdigest())


# CWE-942: Improper Neutralization of Special Elements used in a Command ('Command Injection')
# The vulnerable line is line 2, where user input is directly used to construct a hash object without proper sanitization or validation.