



SERVER  ***************************

For the server, please use the command
chmod +x  chatserve   

before using the server app.


Usage for server is:
./chatserve  <portnum>

example:
./chatserve 55500

Note: Server is written in python 2.7

Also, server app will ask user for a handle BEFORE accepting any connections.


CLIENT **********************

Compiling instructions:
gcc -o chatclient chatclient.c


Usage for client is:

./chatclient flip1.engr.oregonstate.edu <port number>
(note that it can be flip1, flip2, etc. Whichever flip server the chatserver is running on)

Terminating the program ****************

Client end: if client enters "quit". The client app will terminate

Server end:  If server enters "quit", the serve will close the connection, but
remain open to get new connections.   A message is sent to the client notifying that
the server is no longer in connection. Thus the client app will terminate.


Notes and references **************************** 
