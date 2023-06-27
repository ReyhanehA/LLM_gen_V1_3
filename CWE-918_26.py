#7.# Example 7: CWE-918 - Insecure Coding Practices


import os

filename = input("Enter a filename: ")
os.system("ls " + filename)


# The vulnerable line is os.system("ls " + filename) which allows for arbitrary command execution.