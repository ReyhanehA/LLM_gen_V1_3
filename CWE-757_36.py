#7.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if not isinstance(my_set, set):
# Description: This code does not properly check for the exceptional condition where my_set is not a set.
my_set = "hello"
if isinstance(my_set, set):
    print("my_set is a set")
else:
    print("my_set is not a set")