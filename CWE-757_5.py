#6.# CWE-757: Improper Check or Handling of Exceptional Conditions
# Vulnerable line: line 5
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y