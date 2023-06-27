#3.# Example 3: CWE-798 - Use of Insecure Random Number Generator

import random

password = ""
for i in range(8):
    password += str(random.randint(0, 9)) # vulnerable line
print("Your password is:", password)