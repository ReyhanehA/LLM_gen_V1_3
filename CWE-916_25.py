#6.# Example 6: CWE-916 - Use of Hard-coded SSH Credentials
ssh_username = "root"
ssh_password = "password123" # vulnerable line
# This code is vulnerable to CWE-916 as it uses hard-coded SSH credentials which can be easily guessed or exploited by attackers.