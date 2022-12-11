import numpy as np

def makeField(prime: int):
    table = [[0] * prime] * prime
    table = np.array(table)

    for i in range(prime):
        for j in range(prime):
            table[i][j] = (i * j) % prime
    print(table)
    return table

def testGenerators(value: int, field: int) -> bool:
    for i in range(1,field):
        if pow(value, i, field) == 1:
            if i == field-1:
                return True
            return False

if __name__ == "__main__":
    print("Defualt field to generate: 19")
    fieldTable = makeField(19)
    for i in range(19):
        flag = testGenerators(i, 19)
        if flag:
            print("%d is a generator of prime field 19" % (i))
