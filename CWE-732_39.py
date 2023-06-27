#1.# Example 1:

password = input("Enter your password: ")
if password == "password":
    print("Access granted!")
else:
    print("Access denied!")

# The vulnerable line is line 2, where the password is being compared to a string literal "password" instead of using a secure method like hashing.