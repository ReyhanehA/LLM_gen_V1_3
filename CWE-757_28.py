#9.# Example 9:


import base64

data = input("Enter some base64-encoded data: ")
decoded_data = base64.b64decode(data)

if decoded_data.startswith(b"admin"):
    print("You are an admin!")


# CWE-757: Improper Neutralization of Input During Encoding
# Vulnerable line: decoded_data = base64.b64decode(data)
# Description: The program decodes untrusted base64-encoded data without properly validating or sanitizing it, allowing an attacker to execute arbitrary code.