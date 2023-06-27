#10.# Example 10:

import subprocess

filename = input("Enter a filename: ")
subprocess.call(["rm", filename])

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 3, where the user input is being used to delete a file without proper validation. This can lead to unauthorized deletion of important files.