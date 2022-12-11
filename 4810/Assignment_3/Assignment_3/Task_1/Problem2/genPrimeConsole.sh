#!/usr/bin/bash

declare PRIME variable

# 4 bit prime
PRIME=$(openssl prime -generate -bits 4)
echo "openssl prime -generate -bits 4"
echo "Generated 4-bit Prime number: $PRIME"

# 2048 bit prime
PRIME=$(openssl prime -generate -bits 2048)
echo ""
echo "openssl prime -generate -bits 2048"
echo "Generated 2048-bit Prime number: $PRIME"
echo ""

# check prime in openssl
echo "openssl prime $PRIME"
echo " "
openssl prime $PRIME

echo $PRIME > prime.txt
echo ""

python3 checkPrime.py
