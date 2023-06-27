#7.# CWE-798: Improper Validation of Regular Expression
# Vulnerable line: re.findall('([a-z]+)', input_string)
# Description: The code does not validate if the input string is safe for regular expressions.

import re

input_string = input('Enter string: ')
matches = re.findall('([a-z]+)', input_string)
print(matches)