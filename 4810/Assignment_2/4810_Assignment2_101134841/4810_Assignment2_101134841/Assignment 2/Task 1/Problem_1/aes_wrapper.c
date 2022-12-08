/*******************************************************************************************************************************************
 AES_wrapper
 Secure embedded systems lab, Virginia tech

 Author: Suvarna Mane
 3 November 2011
 Description: This file includes a wrapper to receive plaintext from UART and perform AES-128 on NiosII processor running on Altera DE2-70
 AES encryption function is defined in aes_encrypt.c file
*******************************************************************************************************************************************/
 //Include stdio.h for standard input/output. Used for giving output to the screen.
#include "stdio.h"
#include <stdlib.h>
#include "aes_encrypt.c"


// in - it is the array that holds the plain text to be encrypted.
// key - it is the array that holds the key for encryption.
typedef unsigned char u8;
typedef unsigned int c8;

void main()
{
	u8 key[]   = {0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00};
	u8 in[]   = {0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x00  ,0x01};
	u8 out[16];
	FILE *c_out = fopen("output_cipher", "a+");
	if (c_out == NULL){
		printf("ERROR: Could not open file \n");
		exit(-1);
	}
	c8 cipher[16];

	RijndaelKeySchedule(key);       // set AES round keys
	
	RijndaelEncrypt (in, out);
	
	// printf("Output Cipher: %s \n", out); // Print output to console
	
	fprintf(c_out, "{");
	int len = (int)(sizeof(out)/sizeof(out[0]));
	for(int i = 0; i < len; i++){
		cipher[i] = (int)out[i];
		fprintf(c_out, "%x ", cipher[i]); // Write cipher to file
		printf("%x ", cipher[i]); // Print to console
	}
	fprintf(c_out, "}");
	
	printf("\n");
		
	fclose(c_out); //Close file
}

