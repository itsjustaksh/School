# SYSC 4502 Communications Software
# Assignment 1
# Author: Aksh Ravishankar

# Client.py

# Imports
from socket import *
import sys
import time

encoding = 'utf-8'


def client_packet_send(destAddr: str, destPort: int, message: str) -> None:

    global encoding

    # set up socket using dest addr
    message = bytes(message, encoding)
    address = (destAddr, destPort)

    # Send 10 UDP Messages to dest provided at program launch

    # Init socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    try:
        clientSocket.bind(('127.0.0.1', 12001))
        clientSocket.settimeout(1)
    except Exception as e:
        print("Connection error, could not start program")
        print(e)
        exit(1)

    # Send message
    clientSocket.sendto(message, address)

    # wait for message response
    # once available, gather info needed and print as shown in lab doc
    try:
        retMessage, retAddress = clientSocket.recvfrom(2048)
        print(str(retMessage, encoding),'\n\n')
    except:
        print("Request Timed Out")

    clientSocket.close()


def test_api(destAddr, destPort):
    # Sequence of messages to test with
    messages = ['cars', 'dates', 'check BMWX1', 'reserve BMWX1 Wednesday-2023-02-08', 'check BMWX1',
                'delete BMWX1 Wednesday-2023-02-08', 'check BMWX1', 'reserve BMWX1 Sunday-2023-02-19', 
                'reserve BMWX1 Sunday-2023-02-19', 'check BMWX1', 'delete beemer Sunday-2023-02-19', 
                'reserve BMWX1 Cloosday-2023-02-19', 'check BMWX1', 'delete BMWX1 Sunday-2023-02-19', 'quit']

    # Send each message in sequence and print response, wait half a second between responses
    for message in messages:
        print(f'Request: {message}\nResponse:')
        client_packet_send(destAddr, destPort, message)
        time.sleep(0.5)

def startClientUI():

    while (1):
        commandToSend = input("Insert command to send: ")

        client_packet_send(destAddr, destPort, commandToSend)
        time.sleep(0.5)

        if 'quit' in commandToSend:
            return

if __name__ == "__main__":
    # Read command line for destination port and address
    destAddr = sys.argv[1]
    destPort = int(sys.argv[2])

    test = 0

    if test:
        test_api(destAddr, destPort)
    else:
        startClientUI()
