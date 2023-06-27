#4.# Example 4: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def get_list_element(lst, index):
    if index >= len(lst): # vulnerable line
        print("Index out of range")
    else:
        return lst[index]