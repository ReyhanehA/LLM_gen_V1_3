#7.# CWE-614: Use of Insecure Encryption Algorithm

import base64

message = 'secret message'
key = 'password123'

encrypted_message = base64.b64encode(message.encode('utf-8'))

# The vulnerable line is encrypted_message = base64.b64encode(message.encode('utf-8'))
# This code uses an insecure encryption algorithm (base64), which can be easily decoded by attackers.