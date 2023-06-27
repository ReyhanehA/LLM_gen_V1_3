#8.# CWE-614: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: encrypted_data = base64.b64encode(encrypt(data, key))
# Description: The encryption algorithm being used is known to be broken or risky, which can lead to data leaks.