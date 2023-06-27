#5.# Example 5: CWE-918 - Insecure Coding Practices


import os

filename = input("Enter a filename: ")
os.system("echo " + filename)


# The vulnerable line is os.system("echo " + filename) which allows for arbitrary command execution.