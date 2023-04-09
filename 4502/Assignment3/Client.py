# SYSC 4502 Communications Software
# Assignment 1
# Author: Aksh Ravishankar

# Client.py

# Imports
from functools import cache
import os, shutil
from socket import *
import sys
import time

MAX_CACHE_TIME = 60
CACHE_TIME = 0
ID = os.getpid()

def client_packet_send(destAddr: str, destPort: int, message: str, clientSocket: socket) -> None:

    # set up socket using dest addr
    address = (destAddr, destPort)

    global CACHE_TIME
    global ID

    cachePth = f'.cache\\{ID}'

    # Check cache for info if looking for dates or cars lists
    if 'cars' in message:

        try:
            # Check if cache is still valid
            if time.time() - CACHE_TIME > MAX_CACHE_TIME:
                raise(FileNotFoundError)
            # if found in cache, print from cache
            with open(f'{cachePth}\\cars.txt', 'r') as cars: 
                print("From cache:\n\n")
                for line in cars:
                    print(line)
                cars.close()
        except FileNotFoundError or FileExistsError:
            print("File not found in cache or cache stale, reaching server")
            clientSocket.sendto(message.encode(), address)
            try:
                retMessage = clientSocket.recv(2048)
                print(retMessage.decode(),'\n\n')

                saveCars = open(f'{cachePth}\\cars.txt', 'w')
                saveCars.write(retMessage.decode())
                saveCars.close()

                CACHE_TIME = time.time() - CACHE_TIME
            except TimeoutError as e:
                print("Request Timed Out")

    elif 'dates' in message:
        try:
            if time.time() - CACHE_TIME > MAX_CACHE_TIME:
                raise(FileNotFoundError)
            with open(f'{cachePth}\\dates.txt', 'r') as dates: 
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

                saveDates = open(f'{cachePth}\\cars.txt', 'w')
                saveDates.write(retMessage.decode())
                saveDates.close()

                CACHE_TIME = time.time() - CACHE_TIME
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
    global ID
    if not os.path.isdir(f'.cache\\{ID}'):
        os.makedirs(f'.cache\\{ID}', exist_ok=True)
    # Sequence of messages to test with
    messages = ['cars', 'dates', 'check BMWX1', 'reserve BMWX1 Wednesday-2023-02-08', 'check BMWX1',
                'delete BMWX1 Wednesday-2023-02-08', 'check BMWX1', 'reserve BMWX1 Sunday-2023-02-19', 
                'reserve BMWX1 Sunday-2023-02-19', 'check BMWX1', 'delete beemer Sunday-2023-02-19', 
                'reserve BMWX1 Cloosday-2023-02-19', 'check BMWX1', 'delete BMWX1 Sunday-2023-02-19', 'quit']

    # Init socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(5)

    # Start comms
    if test:
    # Send each message in sequence and print response, wait half a second between responses
        for message in messages:
            print(f'Request: {message}\nResponse:')
            client_packet_send(destAddr, destPort, f'R: {message}', clientSocket, )
            time.sleep(0.5)

        clientSocket.close()
    else:
        # Get user input to send messages
        while (1):
            commandToSend = input("Insert command to send: ")

            client_packet_send(destAddr, destPort, f'R: {commandToSend}', clientSocket)
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
        test = sys.argv[3] == 'True'
    except IndexError:
        test = False
    try:
        start_client_UI(destAddr, destPort, test)
    except KeyboardInterrupt:
        print('Shutting Down, goodbye!')
        try:
            shutil.rmtree(f'.cache\\{ID}', False)
            if len(os.listdir('.cache')) <= 0:
                shutil.rmtree(f'.cache', False)
            print('Cache deleted')
            exit(0)
        except Exception as e:
            exit(1)