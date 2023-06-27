#1.# Example 1:


import os

filename = input("Enter a filename: ")
os.system("rm " + filename)


# CWE-942: Improper Neutralization of Special Elements in a Command ('Command Injection')
# The vulnerable line is line 4, where user input is directly concatenated with a system command without proper sanitization or validation.