#9.# CWE-916: Use of Hard-coded SSH Credentials
# Vulnerable line: ssh_host = "example.com"
# Vulnerable line: ssh_port = 22
# Vulnerable line: ssh_username = "admin"
# Vulnerable line: ssh_password = "password123"
ssh_host = input("Enter SSH host: ")
ssh_port = input("Enter SSH port: ")
ssh_username = input("Enter SSH username: ")
ssh_password = input("Enter SSH password: ")