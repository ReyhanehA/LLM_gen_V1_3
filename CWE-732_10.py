#1.# Example 1:

password = input("Enter your password: ") # CWE-732: Insecure Storage of Credentials
file = open("password.txt", "w")
file.write(password)
file.close()