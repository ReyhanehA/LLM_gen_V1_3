#3.# Example 3:


import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

username = input("Enter a username: ")
password = input("Enter a password: ")

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
cursor.execute(query)


# CWE-798: Use of Hard-coded Credentials
# The vulnerable line is query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'" which concatenates user input into a SQL query without proper validation or sanitization.