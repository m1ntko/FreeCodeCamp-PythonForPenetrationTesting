#!/usr/bin/python3

import socket

# Creating the socket object. AF_INET -> ipv4, socket.SOCK_STREAM -> TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP of the server
host = socket.gethostname()
port = 444

clientsocket.connect((host, port))

# Max of data we are goint to accept
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))