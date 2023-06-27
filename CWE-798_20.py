#1.# Example 1:


import os

filename = input("Enter a filename: ")
os.system("rm " + filename)


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is os.system("rm " + filename) which executes a command with user input without proper validation or sanitization.