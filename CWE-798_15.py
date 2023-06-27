#6.# CWE-798: Use of Hard-coded Database Credentials
# Vulnerable line: conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")
# Description: The database credentials are hard-coded in the code, making them easily accessible to attackers.

import psycopg2

conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT * FROM users")
data = cur.fetchall()