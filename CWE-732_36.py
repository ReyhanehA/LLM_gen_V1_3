#8.# Example 8:

import socket

host = input("Enter a hostname: ")
port = int(input("Enter a port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 5, where the user input is being used to connect to a remote host without proper validation. This can lead to unauthorized access to the remote system.