#3.# CWE-757: Improper Check or Handling of Exceptional Conditions
# Vulnerable line: line 8
try:
    x = int(input("Enter a number: "))
except:
    print("Invalid input")