#10.# Example 10:


import hmac

key = input("Enter a key: ")
message = input("Enter a message: ")
hmac_object = hmac.new(key.encode(), message.encode())

print(hmac_object.hexdigest())


# CWE-942: Improper Neutralization of Special Elements used in a Command ('Command Injection')
# The vulnerable line is line 3, where user input is directly used to construct an HMAC object without proper sanitization or validation.