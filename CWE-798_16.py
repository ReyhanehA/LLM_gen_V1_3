#7.# CWE-798: Use of Hard-coded Secret Keys
# Vulnerable line: secret_key = "mysecretkey"
# Description: The secret key is hard-coded in the code, making it easily accessible to attackers.

import jwt

secret_key = "mysecretkey"
payload = {"user_id": 123}
token = jwt.encode(payload, secret_key, algorithm="HS256")