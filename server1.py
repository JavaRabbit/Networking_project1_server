#!/user/bin/python

# import the socket module
import socket

#create socket object
s = socket.socket()

host = socket.gethostname()

# get a port number
port = 50050


# bind to the port
s.bind((host, port))

s.listen(5)

while True:
 c, addr = s.accept()
 print 'got a connection', addr
 c.send("got a connection")
 c.close()

