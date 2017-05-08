#!/user/bin/python

# Project: Project 1 Networking CS 375
# Program:  Chat Server 
# Language: Python 2.7
# Author: Bonnie Kwong
# Description: a python chat server capable of 
# chatting with a client
# Date: May 7, 2017



# import the socket module
import socket
import sys

# global variable socket
s = socket.socket()

# global handle


# Function to verify that command line arguments are correct
def verifyNumArguments():
  # if no port number is given, show usage and exit
  if len(sys.argv) != 2:
    print "Usage: ./chatserve <portnumber>"
    exit(1)

# Function to initialize socket connection
def initializeConnection():

  host = socket.gethostname()
  print host

  # get a port number
  port = int(sys.argv[1])

  # bind to the port
  s.bind((host, port))



# Get a handle form the user
def getHandle():
  serverHandle = raw_input("Enter a handle name for this server:")
  global fullHandle 
  fullHandle = serverHandle + " >" 


# verify user entered correctnumber of arguments
verifyNumArguments()

# initialize socket
initializeConnection()


# Get a handle for the server
#serverHandle = raw_input("Enter a name for this server:")

getHandle()

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
   
   #  else the client did not want to quit, so get a response from the server`
   print msg
   # get string from user on server side
   response = raw_input(fullHandle)
 
   try:
    n = connection.send(fullHandle + response  )
    
    # if server user decides to quit, send message to client, then close this connection
    if(response == "quit"):
      connection.close()
      print "Now closing this connection\n"
      break  # break out of this loop to wait for new connection
   except socket.error:
    print "you have an error sending. conn is broken"
    sys.exit(1)
   # seems like if n equals 0, it could not send, so connection closed (with quit):

connection.close()

