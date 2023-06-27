#2.# Example 2:


import subprocess

command = input("Enter a command: ")
subprocess.call(command, shell=True)


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is subprocess.call(command, shell=True) which executes a command with user input without proper validation or sanitization.