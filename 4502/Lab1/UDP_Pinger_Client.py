# UDP_Pinger_Server.py 

# Need sys to read command line args
from socket import * 
from datetime import datetime
import sys

def client_packet_send(destAddr: str, destPort: int) -> None:

    # set up socket using dest addr
    # clientSocket.bind(("127.0.0.1", 12001)) 
    message = bytes("Message to send", 'ascii')
    address = (destAddr, destPort)

    # Send 10 UDP Messages to dest provided at program launch
    for i in range(0,10):
        # Init socket
        clientSocket = socket(AF_INET, SOCK_DGRAM) 
        clientSocket.bind((destAddr, 12001)) 
        clientSocket.settimeout(2)

        # Send message 
        startTime = datetime.now()
        clientSocket.sendto(message, address)

        # wait for message response
        # once available, gather info needed and print as shown in lab doc
        try:
            retMessage, retAddress = clientSocket.recvfrom(1024)
            retTime = datetime.now()
            current_time = retTime.strftime("%a %b %d %H:%M:%S %Y")
            print("Reply from" + str(retAddress) + ": Ping " + str(i+1) + " " + current_time)
            print("RTT: " + str(retTime - startTime))
        except:
            print("Request Timed Out")

        clientSocket.close()
    

if __name__ == "__main__":
    # Read command line for destination port and address
    destAddr = sys.argv[1]
    destPort = int(sys.argv[2])

    client_packet_send(destAddr, destPort)