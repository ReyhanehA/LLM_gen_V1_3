#7.# Example 7: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def get_max(lst):
    if len(lst) == 0: # vulnerable line
        print("List is empty")
    else:
        return max(lst)