#2.# Example 2:


import subprocess

command = input("Enter a command: ")
subprocess.call(command, shell=True)


# CWE-942: Improper Neutralization of Special Elements in a Command ('Command Injection')
# The vulnerable line is line 3, where user input is directly passed to the subprocess.call() function without proper sanitization or validation.