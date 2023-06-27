#2.# Example 2:

import os
password = input("Enter your password: ")
os.system("echo " + password + " >> password.txt") # CWE-732: Insecure Storage of Credentials