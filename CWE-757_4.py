#5.# CWE-757: Improper Check or Handling of Exceptional Conditions
# Vulnerable line: line 7
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")