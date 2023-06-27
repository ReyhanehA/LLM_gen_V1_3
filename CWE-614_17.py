#8.# CWE-614: Use of Weak Password Policy

import re

password = 'password123'

if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print('Password does not meet minimum requirements.')

# The vulnerable line is password = 'password123'
# This code uses a weak password policy, allowing users to choose easily guessable passwords.