#4.# Example 4: CWE-918 - Insecure Coding Practices


import subprocess

filename = input("Enter a filename: ")
subprocess.call(["cat", filename])


# The vulnerable line is subprocess.call(["cat", filename]) which allows for arbitrary command execution.