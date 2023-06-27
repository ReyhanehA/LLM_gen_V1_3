#4.# Example 4:

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
cursor.execute(query)

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 7, where the user input is being directly inserted into a SQL query without proper sanitization. This can lead to SQL injection attacks and compromise of the database.