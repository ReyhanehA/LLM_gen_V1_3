#5.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: os.system("chmod " + user_input + " file.txt")
import os
user_input = input("Enter file permission: ")
os.system("chmod " + user_input + " file.txt")