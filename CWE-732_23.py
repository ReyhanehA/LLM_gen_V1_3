#4.# Example 4:

import sqlite3

conn = sqlite3.connect("mydatabase.db") # CWE-732: Incorrect Permission Assignment for Critical Resource
cursor = conn.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

# The vulnerable line is the connect() function, which allows any user to access the database without proper authentication or authorization.