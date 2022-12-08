import numpy as np
import random as rand

def inverse(entry: int, field: int) -> int:
    
    U = [field, 1, 0]
    V = [entry % field, 0, 1]

    U = np.array(U)
    V = np.array(V)

    while int(V[0]) > 0:
        W = U - ((int(U[0])//int(V[0]))*V)
        U = V
        V = W

    # To bring -ve values back into field
    inverse = U[2] % field
    
    return inverse


def validPoints(p: int,d: int) -> list:
    
    allowedPoints = []

    for x in range(p):
        for y in range(p):
            lhs = ((x**2) + (y**2)) % p
            rhs = (1 + ((x**2)*(y**2)*d)) % p
            if lhs == rhs:
                allowedPoints.append((x,y))
    
    return allowedPoints

# TODO: Fix this, doesn't work for non-0 points 
def addition(P1: tuple ,P2: tuple, d: int, p: int) -> tuple:
    
    # Set internal vars to make calculation cleaner
    x1 = P1[0]
    y1 = P1[1]

    x2 = P2[0]
    y2 = P2[1]

    denomX = inverse((1 + d*x1*x2*y1*y2), p)
    denomY = inverse((1 - d*x1*x2*y1*y2), p)

    # Do the math
    x3 = (((x1*y2) + (x2*y1)) % p) * denomX
    y3 = (((y1*y2) - (x1*x2)) % p) * denomY

    # Store the value
    P3 = (int(x3 % p), int(y3 % p))
    
    return P3

def tableGen(p: int, d: int, points: np.ndarray) -> np.ndarray:

    table = [[(None,None)] * len(points)] * len(points)
    table = np.array(table, tuple)
    i = 0; j = 0
    for P1 in points:
        i = 0 if i == len(points) else i
        for P2 in points:
            j = 0 if j == len(points) else j
            table[i][j] = addition(P1, P2, d, p)
            j = (j + 1)
        i = (i + 1)

    return table

def generators(table: np.ndarray, d: int, p: int):
    
    temp = list()
    generators = list() # type: ignore
    column = table[0]
    i = 0
    
    for point in column:
        new = point
        for i in range(len(column)):
            if len(temp) < len(column):
                new = addition(new, point, d, p)
                if new not in temp:
                    temp.append(new)
                else:
                    break
            if len(temp) == len(column): 
                generators.append(point)
        temp = list()
        
    return np.array(generators)

def diffieHellman(x: int, point, d: int, p: int):
    
    P = point

    for i in range(x):
        P = addition(point, P, d, p)

    return P

def example(x: int, y: int, g, d: int, p:int):
    xG = diffieHellman(x, g, d, p)
    yG = diffieHellman(y, g, d, p)

    print("Computed g^x: " + str(xG))
    print("Computed g^y: " + str(yG))

    # Party 1 recieves yG, sends xG
    # Party 2 recieves xG, sends yG

    keyX = diffieHellman(x, yG, d, p)
    keyY = diffieHellman(y, xG, d, p)

    print("(g^x)^y = " + str(keyX) + "(g^y)^x = " + str(keyY))

    if keyX == keyY:
        print("Both parties have a pair of matching keys!")
        return True

    return False




if __name__ == "__main__":

    p = 17
    d = -20

    pointList = np.array(validPoints(p,d), tuple)
    table = tableGen(p, d, pointList)
    gens = generators(table, d, p)

    print("List of valid points: ")
    print(pointList)

    print("Addition table in Z19: ")
    print(table)

    print("List of generators: ")
    print(gens)


    index = rand.randint(0,len(gens) - 1)
    print("Test point: " + str(gens[index]) + ", x = 8, y = 11")
    test = example(8, 11, gens[index], d, p)
    if not test:
        print("Find someone else to talk to")