#1.# Example 1: CWE-798 - Hardcoded Password

password = "password123" # vulnerable line
username = input("Enter your username: ")
if username == "admin" and password == "password123":
    print("Access granted!")
else:
    print("Access denied.")