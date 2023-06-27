#5.# Example 5:


import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

table_name = input("Enter a table name: ")
cursor.execute("DROP TABLE " + table_name)


# CWE-757: Improper Neutralization of SQL Commands
# Vulnerable line: cursor.execute("DROP TABLE " + table_name)
# Description: The user input is not properly sanitized before being used in an SQL query, allowing an attacker to inject additional commands.