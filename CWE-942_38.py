#9.# CWE-942: Improper Neutralization of Special Elements in Data Query Logic
# Vulnerable line: query = "SELECT * FROM users WHERE state='" + state + "'"
# Description: This code is vulnerable to SQL injection attacks as it does not properly sanitize user input.