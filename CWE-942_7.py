#8.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: subprocess.call("mv " + user_input + " new_location/", shell=True)
import subprocess
user_input = input("Enter file to move: ")
subprocess.call("mv " + user_input + " new_location/", shell=True)