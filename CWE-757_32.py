#3.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if not isinstance(x, int):
# Description: This code does not properly check for the exceptional condition where x is not an integer.
x = "hello"
if isinstance(x, int):
    print("x is an integer")
else:
    print("x is not an integer")