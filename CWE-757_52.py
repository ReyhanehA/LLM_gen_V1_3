#5.# Example 5: Buffer Overflow

import ctypes

libc = ctypes.CDLL("libc.so.6")

buffer = "A" * 100
libc.strcpy(buffer, "Hello, world!")

# The vulnerable line is line 5 where a buffer is created without proper bounds checking
# CWE-20: Improper Input Validation
# This code is vulnerable to buffer overflow attacks as it does not properly check the size of the buffer