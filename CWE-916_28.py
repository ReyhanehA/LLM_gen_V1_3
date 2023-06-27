#9.# Example 9: CWE-916 - Use of Hard-coded Google Cloud Credentials
google_username = "admin"
google_password = "password123" # vulnerable line
# This code is vulnerable to CWE-916 as it uses hard-coded Google Cloud credentials which can be easily guessed or exploited by attackers.