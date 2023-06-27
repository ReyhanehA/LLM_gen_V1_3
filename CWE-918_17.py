#8.# CWE-918: Buffer Overflow
# Vulnerable line: buffer = 'A' * 1000
# Description: This code creates a buffer of a fixed size, allowing an attacker to overflow the buffer and execute arbitrary code.
buffer = 'A' * 1000
print(buffer)