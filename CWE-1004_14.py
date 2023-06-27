#5.# CWE-1004: Unintended Execution of Code
# This code uses the eval function to execute user input without proper validation
user_input = input("Enter a command: ")
eval(user_input)