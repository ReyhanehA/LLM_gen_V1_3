#8.# CWE-1004: Unintended Execution of Code
# Vulnerable line: ast.literal_eval(user_input)
import ast
user_input = input("Enter a Python literal: ")
value = ast.literal_eval(user_input)
print(value)