#1.# Example 1:

password = input("Enter your password: ") # CWE-732: Incorrect Permission Assignment for Critical Resource
if password == "admin":
    print("Access granted!")
else:
    print("Access denied.")

# The vulnerable line is the input() function, which allows any user to enter a password without proper authentication or authorization.