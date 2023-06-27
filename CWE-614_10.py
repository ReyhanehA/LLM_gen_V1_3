#1.# CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute

import requests

session = requests.Session()
session.cookies.set('session_id', '12345', secure=False)

# The vulnerable line is session.cookies.set('session_id', '12345', secure=False)
# This code sets a session cookie without the 'Secure' attribute, which means it can be transmitted over an insecure connection.