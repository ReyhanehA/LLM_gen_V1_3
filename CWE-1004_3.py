#4.# CWE-1004: Unintended Execution of Code
# Vulnerable line: subprocess.call(user_input, shell=True)
import subprocess
user_input = input("Enter a command: ")
subprocess.call(user_input, shell=True)