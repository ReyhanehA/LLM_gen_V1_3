#8.# Example 8:

import socket

host = input("Enter a hostname or IP address: ") # CWE-732: Incorrect Permission Assignment for Critical Resource
port = int(input("Enter a port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

message = input("Enter a message: ")
s.sendall(message.encode())

data = s.recv(1024)
print(data.decode())

# The vulnerable line is the input() function, which allows any user to enter a hostname or IP address without proper authentication or authorization.