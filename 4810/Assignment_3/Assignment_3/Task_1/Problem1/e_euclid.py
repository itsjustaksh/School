# Extended euclidian algorithm to find gcd
# Author: Aksh Ravishankar
# Student number: 101134841

import numpy as np

# function to calculate euclidian vector
def extEuclid(val1, val2):
    if val1 == 0 or val2 == 0:
        return 0
    if val1 == val2:
        return val1

    a = max(val1, val2)
    b = min(val1, val2)

    U = [a, 1, 0]
    V = [b, 0, 1]

    U = np.array(U)
    V = np.array(V)
	
    i = 0
    while int(V[0]) > 0:
        W = U - ((int(U[0])//int(V[0]))*V)
        U = V
        V = W
        i += 1


    d = U[0]
    x = U[1]
    y = U[2]

    return (d,x,y)

# Default code
if __name__ == "__main__":
    print("Extended euclidian calculator")
    a = 91261
    b = 117035
    vec = extEuclid(a,b)
    print("For inputs 91261 and 117035: ")
    print("D = %d, x = %d, y = %d\nThis gives: " % (vec[0], vec[1], vec[2]))
    print("(%d * %d) + (%d * %d) = %d" % 
            (vec[1], max(a,b), vec[2], min(a,b), vec[0])
            )
