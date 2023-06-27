#8.# Example 8:

import base64

data = input("Enter some base64-encoded data: ")
decoded_data = base64.b64decode(data)

# The vulnerable line is line 3, where user input is being directly passed to the base64.b64decode() function without any validation, which can lead to injection attacks.