import os
import sys
import CompactFIPS202
import binascii

if __name__ == '__main__':
	# SHA3 224 bit digest
	cipher = CompactFIPS202.SHA3_224(b"Aksh")
	print("Hex digest: ")
	print("".join('{:02x}'.format(x) for x in cipher))
	
