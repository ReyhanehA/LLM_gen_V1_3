#9.# Example 9: CWE-918 - Insecure Coding Practices


import os

filename = input("Enter a filename: ")
os.system("rm -rf " + filename)


# The vulnerable line is os.system("rm -rf " + filename) which allows for arbitrary command execution.