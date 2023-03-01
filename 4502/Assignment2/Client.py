# SYSC 4502 Communications Software
# Assignment 1
# Author: Aksh Ravishankar

# Client.py

# Imports
from socket import *
import sys
import time
import traceback

encoding = 'utf-8'


def client_packet_send(destAddr: str, destPort: int, message: str, clientSocket: socket) -> None:

    global encoding

    # set up socket using dest addr
    address = (destAddr, destPort)

    # Send message
    clientSocket.sendto(message.encode(), address)

    # wait for message response
    # once available, gather info needed and print as shown in lab doc
    try:
        retMessage = clientSocket.recv(2048)
        print(retMessage.decode(),'\n\n')
    except TimeoutError as e:
        print(e)
        print("Request Timed Out")


def start_client_UI(destAddr, destPort, test):
    # Sequence of messages to test with
    messages = ['cars', 'dates', 'check BMWX1', 'reserve BMWX1 Wednesday-2023-02-08', 'check BMWX1',
                'delete BMWX1 Wednesday-2023-02-08', 'check BMWX1', 'reserve BMWX1 Sunday-2023-02-19', 
                'reserve BMWX1 Sunday-2023-02-19', 'check BMWX1', 'delete beemer Sunday-2023-02-19', 
                'reserve BMWX1 Cloosday-2023-02-19', 'check BMWX1', 'delete BMWX1 Sunday-2023-02-19', 'quit']

    # Init socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(5)
    clientSocket.sendto('newCon'.encode(), (destAddr, destPort))
    while 1:
        try:
            # Get connection information
            newPort, addr = clientSocket.recvfrom(1024)
            newPort = int(newPort.decode())
            break

        except ValueError:
            clientSocket.sendto('newCon'.encode(), (destAddr, destPort))
            continue
        except TimeoutError as e:
            print("Connection error, could not start program")
            print(e)
            exit(1)

    # Start comms
    if test:
    # Send each message in sequence and print response, wait half a second between responses
        for message in messages:
            print(f'Request: {message}\nResponse:')
            client_packet_send(addr[0], newPort, message, clientSocket)
            time.sleep(0.5)

        clientSocket.close()
    else:
        # Get user input to send messages
        while (1):
            commandToSend = input("Insert command to send: ")

            client_packet_send(addr[0], newPort, message, clientSocket)
            if 'quit' in commandToSend.lower():
                clientSocket.close()
                return
            
            time.sleep(0.5)

if __name__ == "__main__":
    # Read command line for destination port and address
    try:
        destAddr = sys.argv[1]
        destPort = int(sys.argv[2])
    except ValueError as ve:
        print(f'Invalid port number: {sys.argv[2]}')
        exit(1)
    except IndexError as ie:
        print('Missing arguments. Usage: \'python Client.py <Dest Addr> <Port Num>\'')
        exit(1)

    test = 1
    start_client_UI(destAddr, destPort, test)
    exit(0)
    
