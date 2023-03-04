# SYSC 4502 Communications Software
# Assignment 1
# Author: Aksh Ravishankar

# Imports
from random import randint
from socket import *
import struct
from threading import Lock, Thread, Event, get_native_id
import sys
from time import sleep

event = Event()
dataLock = Lock()

class Server:

    def __init__(self, portNum=62002, mulIP='224.0.0.10') -> None:
        '''
        Initiate class and populate data structures from text files (database)
        '''
        
        self.port = portNum
        self.mulGroup = mulIP
        self.serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.encoding = 'utf-8'
        self.threads = []
        self.resListFilepath = 'reservations.txt'
        self.delayOn = False

        # Assign IP address and port number to socket
        # using loopback address
        try:
            self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            group = inet_aton(self.mulGroup)
            bytePack = struct.pack('4sL', group, INADDR_ANY)
            self.serverSocket.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, bytePack)
            self.serverSocket.settimeout(5)
            self.serverSocket.bind(('', self.port))

            print(f'Starting Server... \nWait until "Database loaded" is printed to start other Servers/Clients')
        except:
            print("Connection error, could not start program")
            exit(1)


    def connect(self, dataList): 
        '''
        Open a socket to recieve connections and wait for requests. As they come in, 
        accept and create thread to deal with them. Also use multicast to communicate 
        with other servers for file updates
        '''

        print('Database loaded')

        listenSocket = self.serverSocket
        portCounter = self.port
        while True:
            try:
                # Wait for conn and accept
                message, (ip, portIn) = listenSocket.recvfrom(1024)


                if  'Update File' in message.decode():
                    self.saveData(dataList)
                    listenSocket.sendto(f'{get_native_id()}: DB updated'.encode(), (self.mulGroup, self.port))
                elif 'DB updated' in message.decode():
                    continue

                else:
                    print(f'Request {message} from {ip} on port {portIn}, starting new thread')

                    # Create thread to deal with request 
                    newThread = Thread(target=self.waitForRequests, args=(dataList, message.decode(), ip, portIn, listenSocket))
                    newThread.start()
                    self.threads.append(newThread)

            except TimeoutError:
                try:
                    continue
                except KeyboardInterrupt:
                    event.set()
                    break

        for t in self.threads:
            t.join()

    def waitForRequests(self, dataList, message, dest, port, connSocket) -> None:
        '''
        Remain idle until requests arrive, handle requests as needed. Once request has been handled, 
        return to waiting for requests. If quit command arrives, shut down gracefully. 
        '''

        if event.is_set():
            print('Keyboard interrupt recieved, shutting down thread.')
            self.saveData(dataList)
            return

        
        # Run corresponding action based on message from client.
        # Message is assumed to have the correct format, but not correct
        # data. 
        # See function calls for detials of request handling
        match message.strip().split()[0].lower():
            case 'cars':
                returnMessage = self.composeCarMessage(dataList)

            case 'dates':
                returnMessage = self.composeDateMessage(dataList)

            case 'check':
                car = message.split()[1]
                
                returnMessage = self.composeResMessage(car, dataList)

            case 'reserve':
                car = message.split()[1]
                date = message.split()[2]

                returnMessage = self.addRes((car, date), dataList)
            
            case 'delete':
                car = message.split()[1]
                date = message.split()[2]

                returnMessage = self.deleteRes(car, date, dataList)

            case 'quit':
                connSocket.sendto('Connection terminated.'.encode(), (dest,port))
                self.saveData(dataList)

                print(f"Closing connection with {dest} on {port}, thread ending")

                # Exit thread
                return 

            case _:
                returnMessage = 'Invalid request'
                return

        if self.delayOn:
            delay = randint(a=5, b=10)
            sleep(delay)
        print(f'Sending response and closing thread\n')
        connSocket.sendto(returnMessage.encode(), (dest,port))
        
        return

    def composeCarMessage(self, dataList):
        '''
        Compose reply for cars command by returning a string of all the cars available
        separated by spaces
        '''
        message = ''
        with dataLock:
            for c in dataList[0]:
                message += f'{c} '
        return message

    def composeDateMessage(self, dataList):
        '''
        Compose reply for dates command by returning a string of all the dates available
        for reservation separated by spaces
        '''
        message = ''
        with dataLock:
            for d in dataList[1]:
                message += f'{d} '
        return message

    def composeResMessage(self, car: str, dataList):
        '''
        Compose reply for check command by returning a string of all the reservations booked for 
        for a specific car separated by spaces

        Parameters: 
            car: A string representing the car for which reservations are being checked
        
        '''
        message = ''
        with dataLock:
            if car not in dataList[2].keys() or len(dataList[2][car]) == 0:
                message = f'No Reservations for {car}'
            else:
                for res in dataList[2][car]:
                    message += f'{car} {res}\n'

        return message if message != '' else 'No Reservations for {car}'

    def addRes(self, resMessage, dataList) -> bytes:
        '''
        Check to make sure reservation is valid and add to reservation list. If valid, return 
        a confirmation message. If invalid, return a descriptive error message 
        '''
        car = resMessage[0]
        date = resMessage[1]
        with dataLock:

            if car not in dataList[0]:
                returnMessage = 'Invalid car'
            elif date not in dataList[1]:
                returnMessage = 'Invalid reservation date'
            elif car in dataList[2].keys() and date in dataList[2][car]:
                returnMessage = f'{car} unavailable on {date}, please pick a different car or date'
            else:
                returnMessage = 'Reservation Confirmed'

                if car not in dataList[2].keys():
                    dataList[2][car] = [date]
                else:
                    dataList[2][car] += [date]

        return returnMessage

    def deleteRes(self, car: str, date: str, dataList) -> bytes: 
        '''
        Check to make sure reservation is valid and delete from reservation list. If valid, return 
        a confirmation message. If invalid, return a descriptive error message.
        '''
        with dataLock:
            if car not in dataList[0]:
                returnMessage = 'Invalid car'
            elif date not in dataList[1]:
                returnMessage = 'Invalid reservation date'
            elif car not in dataList[2].keys() or date not in dataList[2][car]:
                returnMessage = f'No reservation booked for {car} on {date}'
            else:
                i = dataList[2][car].index(date)
                dataList[2][car].pop(i)
                returnMessage = f'Reservation for {car} on {date} cancelled.'

        return returnMessage

    def saveData(self, dataList):
        '''
        Write contents of reservation management dictionary to file, remove existing content of file and 
        replace with content from server execution. 
        '''
        with dataLock:
            with open(self.resListFilepath, 'w') as resFile:
                for car in dataList[2].keys():
                    for date in dataList[2][car]:
                        resFile.write(f'{car} {date}\n')

    def start(self):
        # Send multicast message and wait for all clear to read text 
        # files with updated info

        print("Checking for active servers before reading file")
        pid = get_native_id()
        multicast_addr = (self.mulGroup, self.port)
        self.serverSocket.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, struct.pack('b', 1))
        self.serverSocket.sendto(f'{pid}: Update File'.encode(), multicast_addr)

        # Wait for multicast responses, if valid or timeout, start. 
        message = self.serverSocket.recv(1024)
        try:
            while(str(pid) in message.decode()):
                message = self.serverSocket.recv(1024)
            if "DB updated" not in message.decode():
                raise(ValueError)
            print("Recieved file update notification")
        except ValueError:
            print(f"Bad reply from multicast server, cannot start system\nReceived: {message}")
            self.serverSocket.close()
            return None
        except TimeoutError:
            print("No servers responded to broadcast, starting assuming file is ready")

        
        # Filepaths to read initial information from and update
        carListFilepath = r'cars.txt'
        dateListFilepath = r'dates.txt'
        resListFilepath = r'reservations.txt'

        # Data structures
        dataStruct = [[], [], {}]

        try:
            # Read text files, store info in data structure

            # Read existing reservations at startup and store in dictionary. 
            #  Use cars as keys, if car not in dict already, add with res value. Else 
            #  if car in dict add date to that car entry
            with dataLock:
                with open(resListFilepath, 'r') as resFile:
                    for line in resFile:
                        line = line.strip().split(' ')
                        if line[0] not in dataStruct[2].keys():
                            dataStruct[2][line[0]] = [line[1]]
                        else:
                            dataStruct[2][line[0]] += [line[1]]

                # Read info from car list and date list files and store in local data structures
                
                with open(carListFilepath, 'r') as carFile:
                    for car in carFile:
                        dataStruct[0].append(car.strip())

                with open(dateListFilepath, 'r') as dateFile:
                    for date in dateFile:
                        dataStruct[1].append(date.strip())
        except IOError as e:
            print(e)
            exit(2)
        except Exception as e:
            print(e)
            exit(1)

        return dataStruct
            
        

if __name__ == "__main__":
    port_num = None

    try:
        mulCastIP = sys.argv[1]
        port_num = int(sys.argv[2])
    except ValueError as e:
        print("Invalid port number: ", sys.argv[1])
        print("Using default 62002")
    except IndexError as e:
        print("Missing required positional arguments")
        print("Usage: python Server.py <multicast IP> <port number>")
        exit(1)
    
    # Start server
    server = Server(portNum=port_num, mulIP=mulCastIP)
    try:
        data = server.start()
        if data:
            server.connect(data)
    except KeyboardInterrupt:
        server.saveData(data)
    except Exception as e:
        print(e)
        print('Ran into fatal error, saving db before shutting down')
        
    try:
        if data:
            server.saveData(data)
    except:
        print('Could not save db, db may not be loaded')

    print("Server Shutting Down")
    exit(0)