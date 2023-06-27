#10.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if not isinstance(my_float, float):
# Description: This code does not properly check for the exceptional condition where my_float is not a float.
if isinstance(my_float, float):
    print("my_float is a float")
else:
    print("my_float is not a float")