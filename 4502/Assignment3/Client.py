# SYSC 4502 Communications Software
# Assignment 1
# Author: Aksh Ravishankar

# Client.py

# Imports
import os, shutil
from socket import *
import sys
import time


def client_packet_send(destAddr: str, destPort: int, message: str, clientSocket: socket) -> None:

    # set up socket using dest addr
    address = (destAddr, destPort)

    # Check cache for info if looking for dates or cars lists
    if 'cars' in message:
        try:
            # if found in cache, print from cache
            with open('.cache\\cars.txt', 'r') as cars: 
                print("From cache:\n\n")
                for line in cars:
                    print(line)
                cars.close()
        except FileNotFoundError or FileExistsError:
            print("File not found in cache, reaching server")
            clientSocket.sendto(message.encode(), address)
            try:
                retMessage = clientSocket.recv(2048)
                print(retMessage.decode(),'\n\n')

                saveCars = open('.cache\\cars.txt', 'w')
                saveCars.write(retMessage.decode())
                saveCars.close()
            except TimeoutError as e:
                print("Request Timed Out")

    elif 'dates' in message:
        try:
            with open('.cache\\dates.txt', 'r') as dates: 
                print('From cache:\n\n')
                for line in dates:
                    print(line)
                dates.close()
        except FileNotFoundError or FileExistsError:
            print("File not found in cache, reaching server")
            clientSocket.sendto(message.encode(), address)
            try:
                retMessage = clientSocket.recv(2048)
                print(retMessage.decode(),'\n\n')

                saveDates = open('.cache\\cars.txt', 'w')
                saveDates.write(retMessage.decode())
                saveDates.close()
            except TimeoutError as e:
                print("Request Timed Out")
    else:
        clientSocket.sendto(message.encode(), address)

        # wait for message response
        # once available, gather info needed and print as shown in lab doc
        try:
            retMessage = clientSocket.recv(2048)
            print(retMessage.decode(),'\n\n')
        except TimeoutError as e:
            print(e)
            print("Request Timed Out")

        while 1:
            try:
                clientSocket.recv(2048)
            except TimeoutError:
                break


def start_client_UI(destAddr, destPort, test):
    os.makedirs('.cache')
    # Sequence of messages to test with
    messages = ['cars', 'dates', 'check BMWX1', 'reserve BMWX1 Wednesday-2023-02-08', 'check BMWX1',
                'delete BMWX1 Wednesday-2023-02-08', 'check BMWX1', 'reserve BMWX1 Sunday-2023-02-19', 
                'reserve BMWX1 Sunday-2023-02-19', 'check BMWX1', 'delete beemer Sunday-2023-02-19', 
                'reserve BMWX1 Cloosday-2023-02-19', 'check BMWX1', 'delete BMWX1 Sunday-2023-02-19', 'quit']

    # Init socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(11)

    # Start comms
    if test:
    # Send each message in sequence and print response, wait half a second between responses
        for message in messages:
            print(f'Request: {message}\nResponse:')
            client_packet_send(destAddr, destPort, message, clientSocket)
            time.sleep(0.5)

        clientSocket.close()
    else:
        # Get user input to send messages
        while (1):
            commandToSend = input("Insert command to send: ")

            client_packet_send(destAddr, destPort, commandToSend, clientSocket)
            if 'quit' in commandToSend.lower():
                clientSocket.close()
                break
            
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

    test = False
    try:
        test = sys.argv[3]
    except IndexError:
        test = False
    try:
        start_client_UI(destAddr, destPort, test)
    except KeyboardInterrupt:
        try:
            shutil.rmtree('.cache', False)
            exit(0)
        except Exception as e:
            exit(1)