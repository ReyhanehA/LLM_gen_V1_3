#2.# CWE-757: Improper Check or Handling of Exceptional Conditions
# Vulnerable line: line 5
def divide(x, y):
    try:
        return x/y
    except:
        return "Cannot divide by zero"