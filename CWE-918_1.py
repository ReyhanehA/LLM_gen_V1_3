#2.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: os.system(command)
import os
command = input("Enter command: ")
os.system(command)