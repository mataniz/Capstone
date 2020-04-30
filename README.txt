Capstone Project: Ciphers and Steganography

This project has two programs, one that will encrpyt the text inside a given file and the other which will decrpyt it. It runs on a command window/terminal like a regular program you would run. 

Pre-requisites: 
-The user needs to have python installed on their device. If python is not installed the following website can help: 
https://www.python.org/downloads/
-Secondly, the user needs to have the image library installed. On the terminal you can type: 'pip install image'. This should help. 

Running the test: 
For the encryption program, to use, on command line type 'python encytionCapstone fileName bigPicture smallPicture'
This program takes in a textFile, reads it, converts the string to binary data and pastes the small image on the bigger
image based on every '1' it would read from the binary data. 
For example: python encyrptionCapstone.py stringData.txt encryptBig.jpg encryptSmall.jpg
After a successful run the terminal should print: Text Encrypted, Encrypted Image Saved

The decryption program reverse engineers the process and tries to generate a binary code that is then converted back to a string
For the decryption program, to use, type python decryptionCapstone.py encryptedImage bigPicture
For example: python decryptionCapstone.py encryptedImage.jpg encryptBig.jpg
After a successful run, the command window should print: The encoded message is: (whatever message you encrypt)



