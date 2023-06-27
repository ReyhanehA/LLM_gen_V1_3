#1.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if x == 0:
# Description: This code does not properly check for the exceptional condition where x is equal to zero.
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")