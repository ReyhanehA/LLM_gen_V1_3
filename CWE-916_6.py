#7.# CWE-916: Use of Hard-coded Database Credentials
# Vulnerable line: username = "admin"
# Vulnerable line: password = "password123"
# Vulnerable line: database = "mydb"
username = input("Enter database username: ")
password = input("Enter database password: ")
database = input("Enter database name: ")