# Algorithm to find exponent values within a field
# Author: Aksh Ravishankar
# Student number: 101134841

import mul_inverse as mi

def fieldPower(base: int, exp: int, field: int) -> int:
    result = 1
    base_new = base
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0: 
    	base_new = mi.inverse(base, field)
    
    # Calculate exponent under mod
    for i in range(0, abs(exp)):
        result *= base_new
        result = result % field

    return result

# Basic case requested in assignment
if __name__ == "__main__":
    res = fieldPower(27,350,569)
    print("27 ^ 350 under mod 569 is: " + str(res))

