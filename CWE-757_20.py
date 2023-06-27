#1.# Example 1:


import os

filename = input("Enter a filename: ")
os.system("rm " + filename)


# CWE-757: Improper Neutralization of Command Injection
# Vulnerable line: os.system("rm " + filename)
# Description: The user input is not properly sanitized before being used in a system command, allowing an attacker to inject additional commands.