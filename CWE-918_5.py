#6.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: exec(user_input)
user_input = input("Enter code: ")
exec(user_input)