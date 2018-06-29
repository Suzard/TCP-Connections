###########################################################################
# @ file        : mail.py
# @ brief       : Python3.x script for a simple mail client
# @ description : This is a simple mail client written to communicate with
#                 an open mail server.
#                 The sample code for this was taken from 
#                 "Computer Networking: A Top-Down Aproach" by Kurose-Ross.
#                 This doesn't have authentication and TLS capabilites.
# @ author      : sushruth(smallipa@uci.edu) and Fred(fahourai@uci.edu)
############################################################################

# import the socket module
from socket import *

# Message to send
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# connect to the local mail server
mailserver = "localhost"

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(("", 5000))
clientSocket.connect((mailserver, 25))

recv = (clientSocket.recv(1024)).decode()
print(recv)

if recv[:3] != '220':
	print("220 reply not received from server.")
	clientSocket.close()
	
# Send HELO command and print server response.
clientSocket.send(b"HELO uci.edu\r\n")
recv1 = (clientSocket.recv(1024)).decode()
print(recv1)
if recv1[:3] != '250':
	print ("250 reply not received from server.")
	clientSocket.close()

# Send MAIL FROM command and print server response.
clientSocket.send(b"MAIL FROM: smallipa@uci.edu\r\n")
recv2 = (clientSocket.recv(1024)).decode()
print(recv2)
if recv2[:3] != '250':
	print("250 reply not received from server.")
	clientSocket.close()

# Send RCPT TO command and print server response.
clientSocket.send(b"RCPT TO: smallipa@uci.edu\r\n")
recv3 = (clientSocket.recv(1024)).decode()
print(recv3)
if recv3[:3] != '250':
	print ("250 reply not received from server.")
	clientSocket.close()

# Send DATA command and print server response.
clientSocket.send(b"DATA\r\n")
recv4 = (clientSocket.recv(1024)).decode()
print(recv4)
if recv4[:3] != '354':
	print("250 reply not received from server.")
	clientSocket.close()

# Send message data.
# Message ends with a single period.
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv5 = (clientSocket.recv(1024)).decode()
print(recv5)
if recv5[:3] != '250':
	print("250 reply not received from server.")
	clientSocket.close()

# Send QUIT command and get server response.
clientSocket.send(b"QUIT")
clientSocket.close()
