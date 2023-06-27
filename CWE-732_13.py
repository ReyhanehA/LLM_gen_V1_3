#4.# Example 4:

import sqlite3
conn = sqlite3.connect('example.db')
password = input("Enter your password: ")
conn.execute("INSERT INTO users (password) VALUES ('" + password + "')") # CWE-732: Insecure Storage of Credentials
conn.commit()
conn.close()