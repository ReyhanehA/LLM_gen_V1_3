#4.# Example 4: CWE-798 - Use of Unvalidated Input

username = input("Enter your username: ")
password = input("Enter your password: ") # vulnerable line
if username == "admin" and password == "password123":
    print("Access granted!")
else:
    print("Access denied.")