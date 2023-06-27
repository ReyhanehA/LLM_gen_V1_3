#2.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: subprocess.call("ls " + user_input, shell=True)
import subprocess
user_input = input("Enter directory to list: ")
subprocess.call("ls " + user_input, shell=True)