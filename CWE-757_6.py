#7.# CWE-757: Improper Check or Handling of Exceptional Conditions
# Vulnerable line: line 8
try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("File not found")