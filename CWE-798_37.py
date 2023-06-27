#8.# Example 8: CWE-798 - Use of Unvalidated Input in Regular Expression

import re

password = input("Enter your password: ")
if re.match("^[a-zA-Z0-9]{8,}$", password): # vulnerable line
    print("Valid password.")
else:
    print("Invalid password.")