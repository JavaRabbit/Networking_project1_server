#!/user/bin/python

# import the socket module
import socket

#create socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
print s

host = socket.gethostname()
#host = "127.0.0.1"
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

