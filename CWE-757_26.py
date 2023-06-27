#7.# Example 7:


import yaml

data = input("Enter some YAML data: ")
yaml.safe_load(data)


# CWE-757: Improper Neutralization of Input During Deserialization
# Vulnerable line: yaml.safe_load(data)
# Description: The program deserializes untrusted YAML data without properly validating or sanitizing it, allowing an attacker to execute arbitrary code.