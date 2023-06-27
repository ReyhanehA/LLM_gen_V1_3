#2.# Example 2: CWE-918 - Insecure Coding Practices


import subprocess

filename = input("Enter a filename: ")
subprocess.call(["rm", filename])


# The vulnerable line is subprocess.call(["rm", filename]) which allows for arbitrary command execution.