#10.# CWE-798: Use of Hard-coded Encryption Algorithms
# Vulnerable line: cipher = DES.new('mysecretpass', DES.MODE_ECB)
# Description: The encryption algorithm is hard-coded in the code, making it difficult to change and potentially exposing sensitive information.

from Crypto.Cipher import DES

cipher = DES.new('mysecretpass', DES.MODE_ECB)
encrypted_data = cipher.encrypt('sensitive data')