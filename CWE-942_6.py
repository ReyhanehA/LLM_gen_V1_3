#7.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: os.system("cp " + user_input + " backup/")
import os
user_input = input("Enter file to copy: ")
os.system("cp " + user_input + " backup/")