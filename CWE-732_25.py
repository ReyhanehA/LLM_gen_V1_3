#6.# Example 6:

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hostname = input("Enter a hostname: ") # CWE-732: Incorrect Permission Assignment for Critical Resource
username = input("Enter your username: ")
password = input("Enter your password: ")

ssh.connect(hostname, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.read().decode())

# The vulnerable line is the input() function, which allows any user to enter a hostname without proper authentication or authorization.