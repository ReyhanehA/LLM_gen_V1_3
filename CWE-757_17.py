#8.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if not isinstance(my_str, str):
# Description: This code does not properly check for the exceptional condition where my_str is not a string.
if isinstance(my_str, str):
    print("my_str is a string")
else:
    print("my_str is not a string")