#6.# Example 6:

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hostname = input("Enter a hostname: ")
username = input("Enter a username: ")
password = input("Enter a password: ")

ssh.connect(hostname, username=username, password=password)

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 8, where the user input is being used to authenticate with an SSH server without proper validation. This can lead to unauthorized access to the server.