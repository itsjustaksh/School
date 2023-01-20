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
    def startUP(self, portNum) -> None:
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

        with open(self.carListFilepath, 'r') as carFile:
            for car in carFile:
                self.carList.append(car.strip())

        with open(self.dateListFilepath, 'r') as dateFile:
            for date in dateFile:
                self.dateList.append(date.strip())

        # Once initial setup is done, wait for requests
        self.waitForRequests()

    def waitForRequests(self) -> None:
        # Remain idle until requests arrive, handle requests as needed
        print(self.carList)
        print(self.dateList)
        print(self.resDict)
        
        
        # Call necessary functions to handle request
        # while True:
        # wait for and respond to requests
        return

if __name__ == "__main__":
    
    try:
        port_num = int(sys.argv[1])
    except ValueError as e:
        print("Invalid port number: ", sys.argv[1])
    except IndexError as e:
        print("Missing port number")
        print("Usage: python Server.py <port number>")
    
    server = Server()
    server.startUP(port_num)