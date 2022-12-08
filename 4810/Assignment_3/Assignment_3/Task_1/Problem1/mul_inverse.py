# Multipicative inverse using Extended Euclidian Algorithm
# Author: Aksh Ravishankar
# Student number: 101134841

import e_euclid as euc

def inverse(operand: int, field: int):
	
	vec = euc.extEuclid(operand, field)
	inverse = vec[2] % field 			# to move -ve values back into field
	
	return inverse
if __name__ == "__main__":
    mul_inverse = inverse(171,271)
    print("The multipicative inverse of 171 in prime field 271 is: " + 
    		str(mul_inverse))

