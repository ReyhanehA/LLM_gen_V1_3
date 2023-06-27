#1.# CWE-942: Improper Neutralization of Special Elements in the Command (‘Command Injection’)
# Vulnerable line: os.system("ping " + user_input)
import os
user_input = input("Enter IP address to ping: ")
os.system("ping " + user_input)