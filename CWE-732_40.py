#2.# Example 2:

import os

filename = input("Enter a filename: ")
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted.")
else:
    print("File not found.")

# The vulnerable line is line 3, where user input is being directly passed to the os.remove() function without any validation, which can lead to directory traversal attacks.