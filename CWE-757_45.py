#7.# Insecure Cryptographic Storage:

# Vulnerable line:
hashed_password = md5(password)

# Description: This code is vulnerable to insecure cryptographic storage as it uses a weak hashing algorithm that can be easily cracked by an attacker.