#3.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: os.system("rm " + user_input)
import os
user_input = input("Enter file to delete: ")
os.system("rm " + user_input)