# UDP_Pinger_Server.py 

# We will need the following module to generate randomized lost packets 

from socket import * 
import sys

# Init socket
clientSocket = socket(AF_INET, SOCK_DGRAM) 

# Read command line for destination port and address
print(sys.argv[0])
destAddr = sys.argv[1]
destPort = int(sys.argv[2])

# set up socket using dest addr
clientSocket.bind(('', destPort)) 
clientSocket.settimeout(1000)
message = "Message to send"

# Send 10 UDP Messages
for i in range(0,10):
    # Send message to dest 
    clientSocket.sendto(bytes(message, "ascii"), destAddr)

    # wait for message response
    try:
        message, destAddr = clientSocket.recvfrom(1024)
    except TimeoutError:
        print("Request Timed Out")

