###############################################################
# @ File        : WebServer.py
# @ Brief       : Python3.x implementation of a single threaded web server
# @ description : This is a simple implementation of a single threaded web server.
#                 The sample code for this implementation has been adapted from
#                 the Book Computer Networking A Top-down approach, by Kurose-Ross
# @ author      : Sushruth (smallipa@uci.edu) & Fred (fahourai@uci.edu)
#################################################################


#import socket module
from socket import *

# create a tCP socket.
# AF_INET : Socket belonging to IPv4 family
# SOCK_STREAM : mentions that the socket is TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
serverSocket.bind(("169.234.63.38", 6789))

# listen for connections from client
serverSocket.listen(1)
while True:
	# Establish the connection
	print ("Ready to serve...")
	# Accept connection from client
	connectionSocket, addr = serverSocket.accept()
	try:
		# wait for a get request from client
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		# Read the file
		f = open(filename[1:], "rb")
		outputdata = f.read()
		#Send one HTTP header line into socket
		connectionSocket.send(b'HTTP/1.1 200 OK \r\n\r\n')
		#Send the content of the requested file to the client
		for i in range(0,len(outputdata)):
			connectionSocket.send(outputdata[i:i+1])
		connectionSocket.send(b'\r\n\r\n')
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
		connectionSocket.send(b'<html><head></head><body><h1>404 Not Found</h1></body></html>')
		connectionSocket.close()
serverSocket.close()
