#2.# Example 2:


import pickle

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user = User("admin", "password")
serialized_user = pickle.dumps(user)

untrusted_data = input("Enter some untrusted data: ")
deserialized_user = pickle.loads(untrusted_data)

if deserialized_user.username == "admin":
    print("You are an admin!")


# CWE-757: Improper Neutralization of Input During Deserialization
# Vulnerable line: deserialized_user = pickle.loads(untrusted_data)
# Description: The program deserializes untrusted data without properly validating or sanitizing it, allowing an attacker to execute arbitrary code.