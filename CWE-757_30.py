#1.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if x == 0:
# Description: This code does not properly check for the exceptional condition where x is equal to 0.
x = 0
if x:
    print("x is not equal to 0")
else:
    print("x is equal to 0")