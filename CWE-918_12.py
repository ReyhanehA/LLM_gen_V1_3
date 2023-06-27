#3.# CWE-918: Command Injection
# Vulnerable line: os.system('ping ' + ip_address)
# Description: This code takes a user input IP address and directly uses it in a system command, allowing an attacker to execute arbitrary commands.
import os

def ping(ip_address):
    os.system('ping ' + ip_address)