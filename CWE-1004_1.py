#2.# CWE-1004: Unintended Execution of Code
# Vulnerable line: exec(user_input)
user_input = input("Enter a Python statement: ")
exec(user_input)