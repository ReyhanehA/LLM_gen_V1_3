#10.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: subprocess.call("grep " + user_input + " file.txt", shell=True)
import subprocess
user_input = input("Enter text to search: ")
subprocess.call("grep " + user_input + " file.txt", shell=True)