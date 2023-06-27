#1.# Example 1: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def divide(a, b):
    if b == 0: # vulnerable line
        print("Cannot divide by zero")
    else:
        return a/b