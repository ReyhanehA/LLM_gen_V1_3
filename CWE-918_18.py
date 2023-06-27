#9.# CWE-918: Integer Overflow
# Vulnerable line: total = 2**31 + 1
# Description: This code performs an integer operation that can result in an overflow, allowing an attacker to manipulate the value.
total = 2**31 + 1
print(total)