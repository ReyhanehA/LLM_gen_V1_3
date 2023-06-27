#3.# Example 3: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def get_file_contents(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError: # vulnerable line
        print("File not found")