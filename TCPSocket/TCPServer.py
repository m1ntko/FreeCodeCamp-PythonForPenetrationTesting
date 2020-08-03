#!/usr/bin/python3

import socket

# Creating the socket object. AF_INET -> ipv4, socket.SOCK_STREAM -> TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '<IP>' If you do not exactly use same method on the client side, you will get the error: socket.error errno 111 connection refused.
host = socket.gethostname()
port = 444

# To bind host and port to server
serversocket.bind(('192.168.1.56', port))

# Set up TCP listener and how many connections/request 
serversocket.listen(3)

while True:
    # Starting connection
    clientsocket, address = serversocket.accept()
    
    # Server text output
    print("Received connection from: %s " % str(address))

    # Message to send to client
    message = 'Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    # Finish connection
    clientsocket.close()