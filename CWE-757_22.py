#3.# Example 3:


import subprocess

command = input("Enter a command: ")
subprocess.call(command, shell=True)


# CWE-757: Improper Neutralization of Command Injection
# Vulnerable line: subprocess.call(command, shell=True)
# Description: The user input is not properly sanitized before being used in a system command, allowing an attacker to inject additional commands.