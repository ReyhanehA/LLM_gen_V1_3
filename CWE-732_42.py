#4.# Example 4:

import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
cursor.execute(query)

# The vulnerable line is line 7, where user input is being directly concatenated into a SQL query, which can lead to SQL injection attacks.