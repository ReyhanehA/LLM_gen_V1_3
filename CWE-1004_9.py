#10.# CWE-1004: Unintended Execution of Code
# Vulnerable line: ctypes.CDLL(user_input)
import ctypes
user_input = input("Enter a library name: ")
lib = ctypes.CDLL(user_input)
print(lib)