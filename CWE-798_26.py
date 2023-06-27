#7.# Example 7:


import os

filename = input("Enter a filename: ")
os.remove(filename)


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is os.remove(filename) which deletes a file specified by user input without proper validation or sanitization.