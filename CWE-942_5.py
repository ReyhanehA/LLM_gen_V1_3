#6.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: subprocess.call("echo " + user_input + " >> file.txt", shell=True)
import subprocess
user_input = input("Enter text to append: ")
subprocess.call("echo " + user_input + " >> file.txt", shell=True)