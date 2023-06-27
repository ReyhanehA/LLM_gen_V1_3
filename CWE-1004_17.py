#8.# CWE-1004: Unintended Execution of Code
# This code uses the subprocess.call function to execute user input without proper validation
user_input = input("Enter a command: ")
subprocess.call(user_input)