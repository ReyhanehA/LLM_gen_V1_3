#2.# CWE-798: Improper Validation of Array Index
# Vulnerable line: def get_element(array, index):
# Description: The function does not validate if the index is within the bounds of the array.

def get_element(array, index):
    return array[index]