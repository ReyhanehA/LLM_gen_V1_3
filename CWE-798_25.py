#6.# Example 6:


import subprocess

filename = input("Enter a filename: ")
subprocess.call(["rm", filename])


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is subprocess.call(["rm", filename]) which executes a command with user input without proper validation or sanitization.