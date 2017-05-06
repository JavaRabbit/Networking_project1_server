#!/user/bin/python

# import the socket module
import socket
import sys

# if no port number is given, show usage and exit
if len(sys.argv) != 2:
  print "Usage: ./chatserve <portnumber>"
  exit(1)

#create socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
print s

host = socket.gethostname()
#host = "127.0.0.1"
print host

# get a port number
#port = 50050
port = int(sys.argv[1])
print sys.argv[1] + " is the port to use"

# bind to the port
s.bind((host, port))

s.listen(5)

# take out this line from while loop
#c, addr = s.accept()

while True:
 c, addr = s.accept()
  
 # get string from user
 response = raw_input("Enter a reply to client:")
 
 #print 'got a connection', addr
 #c.send("got a connection")
 c.send(response)
 
c.close()

