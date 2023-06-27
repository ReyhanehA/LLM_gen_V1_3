#3.# Example 3:

import subprocess

command = input("Enter a command: ") # CWE-732: Incorrect Permission Assignment for Critical Resource
subprocess.call(command)

# The vulnerable line is the input() function, which allows any user to enter a command without proper authentication or authorization.