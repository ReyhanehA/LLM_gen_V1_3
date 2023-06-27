#10.# Example 10: CWE-918 - Insecure Coding Practices


import subprocess

filename = input("Enter a filename: ")
subprocess.call(["rm", "-rf", filename])


# The vulnerable line is subprocess.call(["rm", "-rf", filename]) which allows for arbitrary command execution.