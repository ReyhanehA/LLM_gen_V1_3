#5.# Example 5: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def get_dict_value(dct, key):
    if key not in dct: # vulnerable line
        print("Key not found")
    else:
        return dct[key]