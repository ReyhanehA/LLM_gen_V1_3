#2.# Example 2:

import os

filename = input("Enter a filename: ")
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted.")
else:
    print("File not found.")

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 4, where the file is being deleted without checking if the user has the necessary permissions to do so. This can lead to unauthorized deletion of important files.