#6.# Example 6: CWE-798 - Use of Unvalidated Input in File Path

filename = input("Enter the filename: ") # vulnerable line
with open(filename, 'r') as f:
    print(f.read())