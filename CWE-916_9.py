#10.# CWE-916: Use of Hard-coded AWS Credentials
# Vulnerable line: aws_access_key = "AKIA1234567890"
# Vulnerable line: aws_secret_key = "secretkey"
aws_access_key = input("Enter AWS access key: ")
aws_secret_key = input("Enter AWS secret key: ")