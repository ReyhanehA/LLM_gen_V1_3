#4.# Example 4:


import json

data = input("Enter some JSON data: ")
json.loads(data)


# CWE-757: Improper Neutralization of Input During Deserialization
# Vulnerable line: json.loads(data)
# Description: The program deserializes untrusted JSON data without properly validating or sanitizing it, allowing an attacker to execute arbitrary code.