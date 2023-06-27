#9.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: os.system("tar -czvf " + user_input + ".tar.gz " + user_input)
import os
user_input = input("Enter directory to compress: ")
os.system("tar -czvf " + user_input + ".tar.gz " + user_input)