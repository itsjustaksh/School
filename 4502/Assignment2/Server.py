# SYSC 4502 Communications Software
# Assignment 1
# Author: Aksh Ravishankar

# Imports
from socket import *
import sys


class Server:
    # Filepaths to read initial information from and update
    carListFilepath = r'cars.txt'
    dateListFilepath = r'dates.txt'
    resListFilepath = r'reservations.txt'

    # Data structures
    resDict = dict()
    carList = []
    dateList = []

    # Conn vars
    port = None
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    encoding = 'utf-8'

    def __init__(self, portNum=62002) -> None:
        '''
        Initiate class and populate data structures from text files (database)
        '''

        self.port = portNum

        # Read text files, store info in data structure

        # Read existing reservations at startup and store in dictionary. 
        #  Use cars as keys, if car not in dict already, add with res value. Else 
        #  if car in dict add date to that car entry

        with open(self.resListFilepath, 'r') as resFile:
            for line in resFile:
                line = line.strip().split(' ')
                if line[0] not in self.resDict.keys():
                    self.resDict[line[0]] = [line[1]]
                else:
                    self.resDict[line[0]] += [line[1]]

        
        # Read info from car list and date list files and store in local data structures
        
        with open(self.carListFilepath, 'r') as carFile:
            for car in carFile:
                self.carList.append(car.strip())

        with open(self.dateListFilepath, 'r') as dateFile:
            for date in dateFile:
                self.dateList.append(date.strip())

        print('Database loaded')

        # Assign IP address and port number to socket
        # using loopback address
        try:
            self.serverSocket.bind(('127.0.0.1', self.port))
            print(f'Server running at 127.0.0.1 on port {self.port}')
        except:
            print("Connection error, could not start program")
            exit(1)

    def waitForRequests(self) -> None:
        '''
        Remain idle until requests arrive, handle requests as needed. Once request has been handled, 
        return to waiting for requests. If quit command arrives, shut down gracefully. 
        '''

        socket = self.serverSocket
        while True:
            message, address = socket.recvfrom(1024)
            message = str(message, self.encoding)

            print(f'Recieved {message} from {address}')
            # Run corresponding action based on message from client.
            # Message is assumed to have the correct format, but not correct
            # data. 
            # See function calls for detials of request handling 
            match message.strip().split()[0].lower():
                case 'cars':
                    returnMessage = self.composeCarMessage()

                case 'dates':
                    returnMessage = self.composeDateMessage()

                case 'check':
                    car = message.split()[1]
                    
                    returnMessage = self.composeResMessage(car)

                case 'reserve':
                    car = message.split()[1]
                    date = message.split()[2]

                    returnMessage = self.addRes((car, date))
                
                case 'delete':
                    car = message.split()[1]
                    date = message.split()[2]

                    returnMessage = self.deleteRes(car, date)

                case 'quit':
                    socket.sendto(bytes('Server shutting down', self.encoding), address)
                    socket.close()
                    self.saveOnQuit()
                    return

                case _:
                    returnMessage = 'Invalid request'

            socket.sendto(bytes(returnMessage, self.encoding), address)

    def composeCarMessage(self):
        '''
        Compose reply for cars command by returning a string of all the cars available
        separated by spaces
        '''
        message = ''
        for c in self.carList:
            message += f'{c} '
        return message

    def composeDateMessage(self):
        '''
        Compose reply for dates command by returning a string of all the dates available
        for reservation separated by spaces
        '''
        message = ''
        for d in self.dateList:
            message += f'{d} '
        return message

    def composeResMessage(self, car: str):
        '''
        Compose reply for check command by returning a string of all the reservations booked for 
        for a specific car separated by spaces

        Parameters: 
            car: A string representing the car for which reservations are being checked
        
        '''
        message = ''

        if car not in self.resDict.keys():
            message = f'No Reservations for {car}'
        else:
            for res in self.resDict[car]:
                message += f'{car} {res}\n'

        return message

    def addRes(self, resMessage) -> bytes:
        '''
        Check to make sure reservation is valid and add to reservation list. If valid, return 
        a confirmation message. If invalid, return a descriptive error message 
        '''
        car = resMessage[0]
        date = resMessage[1]

        if car not in self.carList:
            returnMessage = 'Invalid car'
        elif date not in self.dateList:
            returnMessage = 'Invalid reservation date'
        elif car in self.resDict.keys() and date in self.resDict[car]:
            returnMessage = f'{car} unavailable on {date}, please pick a different car or date'
        else:
            returnMessage = 'Reservation Confirmed'

            if car not in self.resDict.keys():
                self.resDict[car] = [date]
            else:
                self.resDict[car] += [date]

        return returnMessage

    def deleteRes(self, car: str, date: str) -> bytes: 
        '''
        Check to make sure reservation is valid and delete from reservation list. If valid, return 
        a confirmation message. If invalid, return a descriptive error message.
        '''
        if car not in self.carList:
            returnMessage = 'Invalid car'
        elif date not in self.dateList:
            returnMessage = 'Invalid reservation date'
        elif car not in self.resDict.keys() or date not in self.resDict[car]:
            returnMessage = f'No reservation booked for {car} on {date}'
        else:
            i = self.resDict[car].index(date)
            self.resDict[car].pop(i)
            returnMessage = f'Reservation for {car} on {date} cancelled.'

        return returnMessage

    def saveOnQuit(self):
        '''
        Write contents of reservation management dictionary to file, remove existing content of file and 
        replace with content from server execution. 
        '''
        with open(self.resListFilepath, 'w') as resFile:
            for car in self.resDict.keys():
                for date in self.resDict[car]:
                    resFile.write(f'{car} {date}\n')
        
        

if __name__ == "__main__":
    port_num = None

    try:
        port_num = int(sys.argv[1])
    except ValueError as e:
        print("Invalid port number: ", sys.argv[1])
    except IndexError as e:
        print("Missing port number")
        print("Usage: python Server.py <port number>")
        exit(1)
    
    # Start server
    server = Server(port_num)
    try:
        server.waitForRequests()
    except Exception as e:
        print(e)
        print('Ran into error, saving file before closing')
        server.saveOnQuit()
    exit(0)