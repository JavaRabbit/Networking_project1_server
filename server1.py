#!/user/bin/python

# import the socket module
import socket
import sys

#create socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
print s

#host = socket.gethostname()
host = "127.0.0.1"


# get a port number
#port = 50050
port = int(sys.argv[1])
print sys.argv[1] + " is the port to use"

# bind to the port
s.bind((host, port))

s.listen(5)

while True:
 c, addr = s.accept()
 print 'got a connection', addr
 c.send("got a connection")
 c.close()

