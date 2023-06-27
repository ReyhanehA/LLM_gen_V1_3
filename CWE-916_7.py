#8.# CWE-916: Use of Hard-coded SMTP Credentials
# Vulnerable line: smtp_server = "smtp.example.com"
# Vulnerable line: smtp_port = 587
# Vulnerable line: username = "admin"
# Vulnerable line: password = "password123"
smtp_server = input("Enter SMTP server: ")
smtp_port = input("Enter SMTP port: ")
username = input("Enter SMTP username: ")
password = input("Enter SMTP password: ")