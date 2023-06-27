#10.# CWE-798: Improper Validation of Email Input
# Vulnerable line: email = input('Enter email: ')
# Description: The code does not validate if the input is a valid email address.

import re

email = input('Enter email: ')
if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
    print('Valid email')
else:
    print('Invalid email')