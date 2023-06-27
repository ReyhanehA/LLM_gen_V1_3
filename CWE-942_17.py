#8.# Example 8:


import base64

data = input("Enter some data: ")
encoded = base64.b64encode(data)

print(encoded)


# CWE-942: Improper Neutralization of Special Elements used in an Encoding Operation ('Encoding Injection')
# The vulnerable line is line 2, where user input is directly used to encode data without proper sanitization or validation.