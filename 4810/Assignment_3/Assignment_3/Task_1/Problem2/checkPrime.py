from sympy import isprime

if __name__ == "__main__":
    with open('prime.txt', 'r') as primeFile:
        primeNum = int(primeFile.read().replace('\n', ''))
    
    print("Check if number generated is prime using python")
    print("\nNum to check: " + str(primeNum))
    print("\nResult: " + str(isprime(primeNum)))
