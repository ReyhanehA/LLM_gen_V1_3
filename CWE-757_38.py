#9.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if not isinstance(my_list, list):
# Description: This code does not properly check for the exceptional condition where my_list is not a list.
my_list = {"hello"}
if isinstance(my_list, list):
    print("my_list is a list")
else:
    print("my_list is not a list")