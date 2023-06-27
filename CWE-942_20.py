#1.# CWE-942: Improper Neutralization of Special Elements in Data Query Logic
# Vulnerable line: query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
# Description: This code is vulnerable to SQL injection attacks as it does not properly sanitize user input.