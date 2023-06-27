#5.# CWE-1004: Unintended Execution of Code
# Vulnerable line: pickle.loads(user_input)
import pickle
user_input = input("Enter a pickled object: ")
obj = pickle.loads(user_input)
print(obj)