#3.# Example 3:

import subprocess

command = input("Enter a command: ")
subprocess.call(command)

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 3, where the user input is being executed as a command without proper validation. This can lead to arbitrary code execution and compromise of the system.