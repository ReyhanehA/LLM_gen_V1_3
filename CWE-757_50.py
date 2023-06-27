#3.# Example 3: Command Injection

import os

filename = input("Enter a filename: ")
os.system("cat " + filename)

# The vulnerable line is line 3 where user input is concatenated into a shell command
# CWE-20: Improper Input Validation
# This code is vulnerable to command injection attacks as it does not properly sanitize user input