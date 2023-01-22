# Need sys to read command line args
from socket import *
import sys, os


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
    def startUP(self, portNum=12000) -> None:
        '''
        Initiate class and populate data structures from text files (database)
        '''

        self.port = portNum

        # Read text files, store info in data structure

        ''' Read existing reservations at startup and store in dictionary. 
         Use cars as keys, if car not in dict already, add with res value. Else 
         if car in dict '''
        
        with open(self.resListFilepath, 'r') as resFile:
            for line in resFile:
                line = line.strip().split(' ')
                if line[0] not in self.resDict.keys():
                    self.resDict[line[0]] = [line[1]]
                else:
                    self.resDict[line[0]] += [line[1]]

        '''
        Read info from car list and date list files and store in local data structures
        '''
        with open(self.carListFilepath, 'r') as carFile:
            for car in carFile:
                self.carList.append(car.strip())

        with open(self.dateListFilepath, 'r') as dateFile:
            for date in dateFile:
                self.dateList.append(date.strip())

        # Assign IP address and port number to socket 
        # using loopback address
        self.serverSocket.bind(('127.0.0.1', self.port)) 

        # Once initial setup is done, wait for requests
        self.waitForRequests()

    def waitForRequests(self) -> None:
        # Remain idle until requests arrive, handle requests as needed
        # print(self.carList)
        # print(self.dateList)
        # print(self.resDict)

        socket = self.serverSocket
        while True:    
            message, address = socket.recvfrom(1024)

            match message.split()[0]:
                case 'cars':
                    returnMessage = self.composeCarMessage()
                    socket.sendto(returnMessage, address)
                
                case 'dates':
                    returnMessage = self.composeDateMessage()
                    socket.sendto(returnMessage, address)
                
                case 'check':
                    returnMessage = self.composeResMessage()
                    socket.sendto(returnMessage, address)
                
                case 'reserve':
                    car = message.split[1]
                    date = message.split[2]
                    if car not in self.resDict.keys() and car not in self.carList:
                        returnMessage = 'Invalid car'
                        socket.sendto(bytes(returnMessage), address)
                    if date not in self.dateList:
                        returnMessage = 'Invalid reservation date'
                        socket.sendto(bytes(returnMessage), address)
                    
                    self.addRes((car, date))
                    
                    socket.sendto(bytes('Reservation Confirmed'), address)
                case 'delete':
                    
                    # TODO: Implement delete code and function 
                    
                    socket.sendto(bytes('Reservation Deleted'), address)

                case 'quit':

                    # TODO: Implement quit code and function

                    socket.sendto(bytes('Server shutting down'), address)
                    return


    def composeCarMessage(self):
        cList = self.carList
        message = []
        for c in cList:
            message.append(bytes(c, 'utf-8'))
        return message

    def composeDateMessage(self):
        dList = self.dateList
        message = []
        for d in dList:
            message.append(bytes(d, 'utf-8'))
        return message
    
    def composeResMessage(self):
        resMessage = []
        rList = self.resDict
        resCars = rList.keys()

        for car in resCars:
            resMessage.append(bytes(car, 'utf-8'))
            for res in rList[car]:
                resMessage.append(bytes(res, 'utf-8'))

        return resMessage

    def addRes(self, resMessage):
        car = resMessage[0]
        date = resMessage[1]

        if car not in self.resDict.keys():
            self.resDict[car] = [date]
        else:
            self.resDict[car] += [date]

        return

if __name__ == "__main__":
    port_num = None

    try:
        port_num = int(sys.argv[1])
    except ValueError as e:
        print("Invalid port number: ", sys.argv[1])
    except IndexError as e:
        print("Missing port number")
        print("Usage: python Server.py <port number>")
    
    server = Server()
    server.startUP(port_num)