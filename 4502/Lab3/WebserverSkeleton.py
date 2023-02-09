# Import socket module
import os
from socket import * 
import sys

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

# serverIP = "172.17.62.226"
serverIP = "127.0.0.1"
serverPort = 7777

serverSocket = socket(AF_INET, SOCK_STREAM)

#Fill in start 
serverSocket.bind((serverIP, serverPort))
#Fill in end 

# Server should be up and running and listening to the incoming connections

while True:
	print('The server is ready to receive')
	serverSocket.listen()
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end 

	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receives the request message from the client

		message = connectionSocket.recv(2048) #Fill in start        #Fill in end 

		# print complete message received from browser (for information purposes)
		print(message)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1] (when splitting on whitespace)
		filename = message.split()[1].decode()
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open((filename[1:]), mode='r')
		
		# Store the entire content of the requested file in a temporary buffer
		outputdata = f.read() #Fill in start  #Fill in end 

		# Send the HTTP response header line to the connection socket
		
		#Fill in start 
		response = bytearray("HTTP/1.0 200 OK\n\n", 'utf-8')
		outputdata = response + bytearray(outputdata, 'utf-8')
		#Fill in end 
		
		# # Send the content of the requested file to the connection socket
		connectionSocket.sendall(outputdata) 
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError as e:
		# Send HTTP response message for file not found
		print(e)
		#Fill in start 
		message = bytearray('HTTP/1.0 404 File-Not-Found\n\n', 'utf-8')
		connectionSocket.sendall(message)
		#Fill in end 
		
		# Close the client connection socket
		
		#Fill in start 
		connectionSocket.close()
		#Fill in end 
serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
