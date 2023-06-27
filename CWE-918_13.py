#4.# CWE-918: SQL Injection
# Vulnerable line: cursor.execute('SELECT * FROM users WHERE username = ' + username)
# Description: This code takes a user input username and directly uses it in a SQL query, allowing an attacker to manipulate the query and access unauthorized data.
import sqlite3

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ' + username)
    user = cursor.fetchone()
    return user