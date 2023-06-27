#10.# Example 10:


import subprocess

filename = input("Enter a filename: ")
subprocess.call(["rm", filename])


# CWE-757: Improper Neutralization of Command Injection
# Vulnerable line: subprocess.call(["rm", filename])
# Description: The user input is not properly sanitized before being used in a system command, allowing an attacker to inject additional commands.