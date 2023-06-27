#1.# Example 1:

password = input("Enter your password: ")
if password == "password":
    print("Access granted!")
else:
    print("Access denied!")

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 2, where the password is being compared to a string literal "password". This is a weak password and can be easily guessed or brute-forced.