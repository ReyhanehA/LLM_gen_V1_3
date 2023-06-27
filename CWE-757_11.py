#2.# CWE-757: Improper Check for Unusual or Exceptional Conditions
# Vulnerable line: if len(my_list) > 0:
# Description: This code does not properly check for the exceptional condition where my_list is empty.
if my_list:
    print("my_list is not empty")
else:
    print("my_list is empty")