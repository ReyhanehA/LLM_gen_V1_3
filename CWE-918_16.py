#7.# CWE-918: Improper Input Validation
# Vulnerable line: if len(password) < 8:
# Description: This code checks the length of a user input password, but does not validate the input for other potential vulnerabilities.
def validate_password(password):
    if len(password) < 8:
        return False
    return True