#8.# CWE-757: Improper Check or Handling of Exceptional Conditions
# Vulnerable line: line 6
def open_file(filename):
    try:
        f = open(filename, "r")
        return f.read()
    except FileNotFoundError:
        return "File not found"