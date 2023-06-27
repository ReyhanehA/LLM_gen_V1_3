#6.# Example 6: CWE-918 - Insecure Coding Practices


import subprocess

filename = input("Enter a filename: ")
subprocess.call(["echo", filename])


# The vulnerable line is subprocess.call(["echo", filename]) which allows for arbitrary command execution.