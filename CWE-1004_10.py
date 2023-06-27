#1.# CWE-1004: Unintended Execution of Code
# This code takes user input and executes it without proper validation
user_input = input("Enter a command: ")
eval(user_input)