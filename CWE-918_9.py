#10.# CWE-918: Insecure Interaction Between Components
# Vulnerable line: sqlite3.connect(database)
import sqlite3
database = input("Enter database path: ")
conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())