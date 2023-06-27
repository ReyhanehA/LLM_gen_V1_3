#5.# CWE-614: Use of Insufficiently Random Values

import random

password = str(random.randint(1000, 9999))

# The vulnerable line is password = str(random.randint(1000, 9999))
# This code generates a password using insufficiently random values, which can be easily guessed by attackers.