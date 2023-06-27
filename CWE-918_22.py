#3.# Example 3: CWE-918 - Insecure Coding Practices


import os

filename = input("Enter a filename: ")
os.system("cat " + filename)


# The vulnerable line is os.system("cat " + filename) which allows for arbitrary command execution.