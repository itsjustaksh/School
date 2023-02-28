from socket import *

# Message to send
msg = '\r\nI love computer networks!'
endmsg = '\r\n.\r\n'

# Choose a mail server and call it mailserver
mailserver = '127.0.0.1'

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start   

#Fill in end 

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO SYSC4502\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("After HELO " + recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send MAIL FROM command and print server response.

#Fill in start   

#Fill in end 

# Send RCPT TO command and print server response. 

#Fill in start   

#Fill in end 

# Send DATA command and print server response. 

#Fill in start   

#Fill in end 

# Send message data.

#Fill in start   

#Fill in end 

# Message ends with a single period.

#Fill in start   

#Fill in end 

# Send QUIT command and get server response.

#Fill in start   

#Fill in end 
