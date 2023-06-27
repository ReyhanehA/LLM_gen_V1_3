#4.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: subprocess.call("cat " + user_input, shell=True)
import subprocess
user_input = input("Enter file to read: ")
subprocess.call("cat " + user_input, shell=True)