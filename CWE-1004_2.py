#3.# CWE-1004: Unintended Execution of Code
# Vulnerable line: os.system(user_input)
import os
user_input = input("Enter a command: ")
os.system(user_input)