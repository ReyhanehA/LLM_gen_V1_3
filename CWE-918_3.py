#4.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: eval(user_input)
user_input = input("Enter expression: ")
result = eval(user_input)
print(result)