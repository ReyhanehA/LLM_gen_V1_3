#3.# Example 3:


import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

table_name = input("Enter a table name: ")
cursor.execute("DROP TABLE " + table_name)

conn.commit()
conn.close()


# CWE-942: Improper Neutralization of Special Elements in a Command ('Command Injection')
# The vulnerable line is line 6, where user input is directly concatenated with a SQL command without proper sanitization or validation.