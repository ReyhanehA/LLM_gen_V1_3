#7.# Example 7:


import pickle

class MyClass:
    def __init__(self, name):
        self.name = name

obj = MyClass(input("Enter a name: "))
pickle.dump(obj, open("example.pkl", "wb"))


# CWE-942: Improper Neutralization of Special Elements used in a File Name ('Path Injection')
# The vulnerable line is line 5, where user input is directly used to construct a file name without proper sanitization or validation.