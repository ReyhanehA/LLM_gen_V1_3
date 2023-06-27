#5.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: subprocess.call(command)
import subprocess
command = input("Enter command: ")
subprocess.call(command)