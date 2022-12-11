import os
import sys
import CompactFIPS202

if __name__ == '__main__':
	# SHA3 224 bit digest
	cipher = CompactFIPS202.SHA3_224(b"Aksh")
	print("SHA3-224 digest: ")
	print("".join('{:02x}'.format(x) for x in cipher))
	
	# SHA3 256 bit digest
	cipher = CompactFIPS202.SHA3_256(b"Aksh")
	print("SHA3-256 digest: ")
	print("".join('{:02X}'.format(x) for x in cipher))
	
	# SHA3 384 bit digest
	cipher = CompactFIPS202.SHA3_384(b"Aksh")
	print("SHA3-384 digest: ")
	print("".join('{:02X}'.format(x) for x in cipher))
	
	# SHA3 512 bit digest
	cipher = CompactFIPS202.SHA3_512(b"Aksh")
	print("SHA3-512 digest: ")
	print("".join('{:02X}'.format(x) for x in cipher))
