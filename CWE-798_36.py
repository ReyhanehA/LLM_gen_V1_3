#7.# Example 7: CWE-798 - Use of Unvalidated Input in Command Execution

import os

filename = input("Enter the filename: ")
os.system("cat {}".format(filename)) # vulnerable line