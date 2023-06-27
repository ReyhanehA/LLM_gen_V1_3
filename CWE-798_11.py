#2.# CWE-798: Use of Hard-coded Encryption Keys
# Vulnerable line: cipher = AES.new('mysecretpass', AES.MODE_CBC, 'ivparameter')
# Description: The encryption key is hard-coded in the code, making it easily accessible to attackers.

from Crypto.Cipher import AES

cipher = AES.new('mysecretpass', AES.MODE_CBC, 'ivparameter')
encrypted_data = cipher.encrypt('sensitive data')