#8.# Example 8: CWE-918 - Insecure Coding Practices


import subprocess

filename = input("Enter a filename: ")
subprocess.call(["ls", filename])


# The vulnerable line is subprocess.call(["ls", filename]) which allows for arbitrary command execution.