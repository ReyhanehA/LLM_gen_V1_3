#7.# Example 7: CWE-916 - Use of Hard-coded Database Credentials
db_username = "admin"
db_password = "password123" # vulnerable line
# This code uses hard-coded database credentials which can be easily guessed or cracked, making it vulnerable to attacks.