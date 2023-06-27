#1.# CWE-1004: Unintended Execution of Code
# Vulnerable line: eval(user_input)
user_input = input("Enter a mathematical expression: ")
result = eval(user_input)
print("Result:", result)