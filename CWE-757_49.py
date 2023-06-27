#2.# Example 2: SQL Injection

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
c.execute(query)

print(c.fetchall())

# The vulnerable line is line 7 where user input is concatenated into a SQL query
# CWE-20: Improper Input Validation
# This code is vulnerable to SQL injection attacks as it does not properly sanitize user input