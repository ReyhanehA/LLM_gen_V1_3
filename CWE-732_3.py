#4.# Example 4:

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("CREATE TABLE users (username TEXT, password TEXT)") # CWE-732: Insecure Storage of Credentials