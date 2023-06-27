#7.# Example 7:

import hmac
password = input("Enter your password: ")
key = b'secret_key'
h = hmac.new(key, password.encode(), hashlib.sha256)
print(h.hexdigest()) # CWE-732: Insecure Storage of Credentials