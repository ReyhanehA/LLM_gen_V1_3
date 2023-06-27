#6.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if not isinstance(my_tuple, tuple):
# Description: This code does not properly check for the exceptional condition where my_tuple is not a tuple.
my_tuple = "hello"
if isinstance(my_tuple, tuple):
    print("my_tuple is a tuple")
else:
    print("my_tuple is not a tuple")