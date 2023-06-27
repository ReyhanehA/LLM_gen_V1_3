#4.# CWE-798: Use of Hard-coded File Paths
# Vulnerable line: file_path = "/home/user/documents/secret.txt"
# Description: The file path is hard-coded in the code, making it difficult to change and potentially exposing sensitive information.

with open("/home/user/documents/secret.txt", "r") as f:
    data = f.read()