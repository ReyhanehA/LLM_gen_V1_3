#9.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if not isinstance(my_bool, bool):
# Description: This code does not properly check for the exceptional condition where my_bool is not a boolean.
if isinstance(my_bool, bool):
    print("my_bool is a boolean")
else:
    print("my_bool is not a boolean")