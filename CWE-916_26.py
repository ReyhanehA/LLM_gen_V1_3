#7.# Example 7: CWE-916 - Use of Hard-coded AWS Access Key
aws_access_key = "AKIA1234567890" # vulnerable line
# This code is vulnerable to CWE-916 as it uses a hard-coded AWS access key which can be easily guessed or exploited by attackers.