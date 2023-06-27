#5.# Example 5:

import subprocess

command = input("Enter a command: ")
subprocess.call(command)

# The vulnerable line is line 3, where user input is being directly passed to the subprocess.call() function without any validation, which can lead to command injection attacks.