#2.# Example 2:

import os

filename = input("Enter a filename: ") # CWE-732: Incorrect Permission Assignment for Critical Resource
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print("File not found.")

# The vulnerable line is the input() function, which allows any user to enter a filename without proper authentication or authorization.