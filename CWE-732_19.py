#10.# Example 10:

import pyaes
password = input("Enter your password: ")
key = b"secret_key"
aes = pyaes.AESModeOfOperationCTR(key)
encrypted_password = aes.encrypt(password)
file = open("password.txt", "wb")
file.write(encrypted_password) # CWE-732: Insecure Storage of Credentials
file.close()