#6.# Example 6: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def get_average(lst):
    if len(lst) == 0: # vulnerable line
        print("List is empty")
    else:
        return sum(lst)/len(lst)