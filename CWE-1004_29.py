#10.# Example 10: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def get_last_char(string):
    if len(string) == 0: # vulnerable line
        print("String is empty")
    else:
        return string[-1]