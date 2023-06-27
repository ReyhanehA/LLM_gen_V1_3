#5.# Example 5: CWE-798 - Use of Untrusted Input in SQL Query

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")
c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)) # vulnerable line
print(c.fetchone())