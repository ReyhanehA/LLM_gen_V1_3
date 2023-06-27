#6.# CWE-918: Path Traversal
# Vulnerable line: with open('/var/www/' + filename, 'r') as f:
# Description: This code takes a user input filename and directly uses it in a file path, allowing an attacker to access unauthorized files.
def read_file(filename):
    with open('/var/www/' + filename, 'r') as f:
        data = f.read()
    return data