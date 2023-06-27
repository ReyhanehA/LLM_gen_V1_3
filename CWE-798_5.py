#6.# CWE-798: Improper Validation of SQL Query
# Vulnerable line: cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
# Description: The code does not validate if the username input is safe for SQL queries.

import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

username = input('Enter username: ')
cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
print(cursor.fetchall())