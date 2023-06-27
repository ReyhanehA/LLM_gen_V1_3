#1.# CWE-798: Improper Validation of Input to a Function
# Vulnerable line: def calculate_sum(numbers):
# Description: The function does not validate if the input is a list of integers.

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total