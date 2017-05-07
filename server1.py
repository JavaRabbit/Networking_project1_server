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
# print sys.argv[1] + " is the port to use"

# bind to the port
s.bind((host, port))


# first while loop surrounds listem
while True:
  s.listen(5)

  print "Listening for a new connection..."


  # take out this line from while loop
  connection, addr = s.accept()
  print 'Connection from', addr[0]

  while True:
   #connection, addr = s.accept()
 
   #  get what the client entered
   msg = connection.recv(4096)
   # if the msg is quit, it means that client is going to close connectoin
   if msg == "quit\n":
    print "Client has decided to terminate connection. This connection will now close.\n"
    break  # creak out of while loop. 
   print msg
   # get string from user
   response = raw_input("Enter a reply to client:")
 
   # if input from user is "quit", close this connection
   if(response == "quit"):
     print "you want to quit?"

   try:
    n = connection.send(response)
    # print n
    # if server user decides to quit, send message to client, then close this connection
    if(response == "quit"):
      connection.close()
      break  # break out of this loop to wait for new connection
   except socket.error:
    print "you have an error sending. conn is broken"
    sys.exit(1)
   # seems like if n equals 0, it could not send, so connection closed (with quit):

connection.close()

