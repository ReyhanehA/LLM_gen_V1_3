#5.# Example 5: CWE-916 - Use of Hard-coded Database Credentials
db_username = "admin"
db_password = "password123" # vulnerable line
# This code is vulnerable to CWE-916 as it uses hard-coded database credentials which can be easily guessed or exploited by attackers.