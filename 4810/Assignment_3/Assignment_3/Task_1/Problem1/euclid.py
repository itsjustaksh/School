# Euclidian algorithm to find gcd
# Author: Aksh Ravishankar
# Student number: 101134841

def euclid(num1: int, num2: int):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == num2:
        return num1
    if num2 > num1:
        vec = (num1, num2)
    else:
        vec = (num2, num1)

    while vec[0] > 0:
        vec = (vec[1] % vec[0], vec[0])

    return vec[1]

# Default code
if __name__ == "__main__":
	print("Euclidian GCD calculator")
	a = 91261
	b = 117035
	gcd = euclid(a,b)
	print("GCD of %d and %d is: %d" % (a, b, gcd))
