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
    clientSocket.send(message.encode())

    # wait for message response
    # once available, gather info needed and print as shown in lab doc
    try:
        retMessage = clientSocket.recv(2048)
        print(retMessage.decode(),'\n\n')
    except TimeoutError as e:
        print(e)
        print("Request Timed Out")


def test_client(destAddr, destPort):
    # Sequence of messages to test with
    messages = ['cars', 'dates', 'check BMWX1', 'reserve BMWX1 Wednesday-2023-02-08', 'check BMWX1',
                'delete BMWX1 Wednesday-2023-02-08', 'check BMWX1', 'reserve BMWX1 Sunday-2023-02-19', 
                'reserve BMWX1 Sunday-2023-02-19', 'check BMWX1', 'delete beemer Sunday-2023-02-19', 
                'reserve BMWX1 Cloosday-2023-02-19', 'check BMWX1', 'delete BMWX1 Sunday-2023-02-19', 'quit']

    # Init socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.bind(('127.0.0.1', ))

    try:
        # Get connection information
        clientSocket.sendto('newCon'.encode(), (destAddr, destPort))
        newPort, addr = clientSocket.recvfrom(1024)
        newPort = int(newPort.decode())
        clientSocket.close()

        # Connect to server
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((destAddr, newPort))
    except Exception as e:
        print("Connection error, could not start program")
        print(e)
        traceback.print_exc()
        exit(1)

    # Send each message in sequence and print response, wait half a second between responses
    for message in messages:
        print(f'Request: {message}\nResponse:')
        client_packet_send(destAddr, destPort, message, clientSocket)
        time.sleep(0.5)

    clientSocket.close()

def startClientUI(destAddr, destPort):

    # Init socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    try:
        # Connect to server
        clientSocket.sendto('newCon'.encode(), (destAddr, destPort))
        newPort = clientSocket.recv(1024)
        newPort = int(newPort.decode())
        clientSocket.close()

        # Recieve new port to send to
        # Connect to server
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.bind(('127.0.0.1', 12001))
        clientSocket.connect((destAddr, newPort))
    except Exception as e:
        print("Connection error, could not start program")
        print(e)
        exit(1)

    while (1):
        commandToSend = input("Insert command to send: ")

        client_packet_send(destAddr, destPort, commandToSend, clientSocket)
        time.sleep(0.5)

        if 'quit' in commandToSend:
            clientSocket.close()
            return

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

    if test:
        test_client(destAddr, destPort)
        exit(0)
    else:
        startClientUI(destAddr, destPort)
        exit(0)
