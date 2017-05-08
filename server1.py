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
import signal
import time
import os

# global variable socket
s = socket.socket()

##############################
# Function to handle sigint 
def sigint_handler(signum, frame):
 print "Thanks for using the server. Good bye"
 exit(0)

####################################
# Function to verify that command line arguments are correct
def verifyNumArguments():
  # if no port number is given, show usage and exit
  if len(sys.argv) != 2:
    print "Usage: ./chatserve <portnumber>"
    exit(1)

####################################
# Function to initialize socket connection
def initializeConnection():

  host = socket.gethostname()
  print host

  # get a port number
  port = int(sys.argv[1])

  # bind to the port
  s.bind((host, port))


################################
# Get a handle form the user
def getHandle():
  serverHandle = raw_input("Enter a handle name for this server:")
  global fullHandle 
  fullHandle = serverHandle + " >" 



###################################
#  chat function runs a while loop to 
#  receive and send messages to clients
#  the outer while loop listens for connections
# thus if a connection terminates
# it is able to use the same socket
# to connect to new connections
#
####################################
def chat():
  
  # for the sigint handler
  signal.signal(signal.SIGINT, sigint_handler)
  
  # first while loop surrounds listem
  while True:
    s.listen(5)

    print "Listening for a new connection..."

    # accept a new connection from client
    connection, addr = s.accept()
    print 'Connection from', addr[0]

    while True:
 
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
 
     # enclose the send method in a try exception, in case there is
     # a socket error
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

  connection.close()

# verify user entered correctnumber of arguments
verifyNumArguments()

# get a handle from the user
getHandle()

# initialize socket
initializeConnection()

# call the chat function to call chat method
chat()

