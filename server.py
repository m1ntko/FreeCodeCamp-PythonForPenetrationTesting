#!/usr/bin/python3

import socket

# Creating the socket object
# AF_NET -> ipv4, socket.SOCK_STREAM -> TCP
serversocket = socket.socket(socket.AF_NET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

# To bind host and port to server
serversocket.bind(host, port)
# Set up TCP listener and how many connections/request 
serversocket.listen(3)
while True:
    # Starting connection
    clientsocket, address = serversocket.accept()
    
    print("Received connection from: %s " % str(address))
    message = 'Ty for connecting to the server' + "\r\n\"
    clientsocket.send(message)
    clientsocket.close