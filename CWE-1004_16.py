#7.# CWE-1004: Unintended Execution of Code
# This code uses the os.system function to execute user input without proper validation
user_input = input("Enter a command: ")
os.system(user_input)