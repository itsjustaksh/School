#!/bin/bash

# Create CBC Encrypted Pic
#openssl enc -aes-128-cbc -e -in pic_original.bmp -out cipher_cbc.bmp -K 00000000000000000000000000000000 -iv 00000000000000000000000000000000
#head -c 54 pic_original.bmp > header_cbc
#tail -c +55 cipher_cbc.bmp > body_cbc
#cat header_cbc body_cbc > pic_original_cbc.bmp


# Create ECB Encrypted Pic
openssl enc -aes-128-ecb -e -in pic_original.bmp -out cipher_ecb.bmp -K 00000000000000000000000000000000
head -c 54 pic_original.bmp > header_ecb
tail -c +55 cipher_ecb.bmp > body_ecb
cat header_ecb body_ecb > pic_original_ecb.bmp

# Cleanup 
#rm cipher_cbc.bmp
rm cipher_ecb.bmp
#rm header_cbc
rm header_ecb
#rm body_cbc
rm body_ecb

