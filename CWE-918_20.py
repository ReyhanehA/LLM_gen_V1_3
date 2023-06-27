#1.# Example 1: CWE-918 - Insecure Coding Practices


import os

filename = input("Enter a filename: ")
os.system("rm " + filename)


# The vulnerable line is os.system("rm " + filename) which allows for arbitrary command execution.