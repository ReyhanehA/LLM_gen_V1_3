#2.# Example 2: CWE-1004 - Improper Check for Unusual or Exceptional Conditions

def get_user_input():
    user_input = input("Enter a number: ")
    if not user_input.isdigit(): # vulnerable line
        print("Invalid input")
    else:
        return int(user_input)