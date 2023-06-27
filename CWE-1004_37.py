#8.# Example 8: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def get_min(lst):
    if len(lst) == 0: # vulnerable line
        print("List is empty")
    else:
        return min(lst)