#1.# CWE-798: Use of Hard-coded Credentials
# Vulnerable line: password = "password123"
# Description: The password is hard-coded in the code, making it easily accessible to attackers.

password = "password123"
username = "admin"
login(username, password)