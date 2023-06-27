#3.# CWE-798: Improper Validation of Command-Line Arguments
# Vulnerable line: filename = sys.argv[1]
# Description: The code does not validate if the command-line argument is a valid filename.

import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    print(file.read())