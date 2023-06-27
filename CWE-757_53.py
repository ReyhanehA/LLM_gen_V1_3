#1.# CWE-757: Improper Check or Handling of Exceptional Conditions
# Vulnerable line: line 10
try:
    x = 1/0
except:
    print("An error occurred")