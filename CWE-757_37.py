#8.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if not isinstance(my_dict, dict):
# Description: This code does not properly check for the exceptional condition where my_dict is not a dictionary.
my_dict = ["hello"]
if isinstance(my_dict, dict):
    print("my_dict is a dictionary")
else:
    print("my_dict is not a dictionary")