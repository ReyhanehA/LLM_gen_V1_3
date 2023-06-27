#8.# Example 8: CWE-916 - Use of Hard-coded Azure Credentials
azure_username = "admin"
azure_password = "password123" # vulnerable line
# This code is vulnerable to CWE-916 as it uses hard-coded Azure credentials which can be easily guessed or exploited by attackers.