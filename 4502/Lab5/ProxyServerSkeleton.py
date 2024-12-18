from socket import *
import sys
import traceback

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
	
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((sys.argv[1], 8888))
tcpSerSock.settimeout(3)
tcpSerSock.listen()
# Fill in start
# Fill in end

def foo():
	while 1:
		print('Ready to serve...')
		# Start receiving data from the client
		try:
			tcpCliSock, addr = tcpSerSock.accept()
		except TimeoutError:
			continue
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		print('Received a connection from:', addr)
		message = tcpCliSock.recv(1024) # Fill in start    # Fill in end
		# print(message)
		# suppress processing of requests for favicon
		if message.split()[1].decode() == "/favicon.ico":
			print("Suppress request for favicon")
			continue
		filename = message.split()[1].partition("/".encode())[2].decode()
		fileExist = "false"
		filetouse = "/" + filename.replace("/","-")
		print("File to use " + filetouse)
		try:
			# Check wether the file exist in the cache
			f = open(filetouse[1:], "r")
			outputdata = f.readlines()
			fileExist = "true"
			print("Service file from cache")
			# ProxyServer finds a cache hit and generates a response message
			tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
			tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())

			# Fill in start
			for line in outputdata:
				tcpCliSock.send(line.encode())
			tcpCliSock.send("\r\n\r\n".encode())
			# Fill in end

		# Error handling for file not found in cache
		except IOError:
			if fileExist == "false":
				# Create a socket on the proxyserver
				c = socket(AF_INET, SOCK_STREAM) # Fill in start            # Fill in end
				hostn = filename.split("/")[0].replace("www.","",1)
				print("Host " + hostn)

				print("File not in cache, requesting from original server")
				try:
					# Connect to the socket to port 80
					# Fill in start # Fill in end
					c.connect((hostn, 80))
					message = "GET "+"http://" + filename + " HTTP/1.0\r\n\r\n"
					c.send(message.encode())
					# Read the response into buffer
					
					# Fill in start
					response = c.recv(4096)
					tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
					tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
					tcpCliSock.send(response.partition("/html".encode())[2])
					# Fill in end

					# Create a new file in the cache for the requested file. Also send the response in the buffer to client socket and the corresponding file in the cache
					tmpFile = open("./" + filetouse,"w")

					# Fill in start
					tmpFile.write(response.decode().partition("/html")[2].strip())
					tmpFile.close()
					c.close()
					# Fill in end
				except:
					print("Illegal request")
					traceback.print_exc()
			else:
				# HTTP response message for file not found
				
				# Fill in start
				message = 'HTTP/1.0 404 File-Not-Found\r\n\r\n'.encode()
				tcpCliSock.send(message)
				# Fill in end
		
		# Close the client and the server sockets    

		# Fill in start
		tcpCliSock.close()
		# Fill in end
	tcpSerSock.close()

if __name__ == '__main__':
	try:
		foo()
	except KeyboardInterrupt:
		sys.exit(1)
