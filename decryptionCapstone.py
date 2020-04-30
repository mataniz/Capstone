#To use, type python decryptionCapstone.py encryptedImage bigPicture

from PIL import Image, ImageChops, ImageOps
import binascii
import sys

def isBit(img):
 pixels = img.getdata()
 brightness = 0
 for (r, g, b) in pixels:
     brightness += r
     brightness += g
     brightness += b
     return brightness > 100
     
def BinaryToDecimal(binary):  
         
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal) 
		
		
encodedImage = Image.open(sys.argv[1])
orignalImage = Image.open(sys.argv[2])

diff = ImageChops.difference(encodedImage, orignalImage)


diff.save("DifferenceImage.jpg")
cropped = diff.copy()

width, height = encodedImage.size

binaryString = ""

for i in range(1000):
    area = ((50*i) % width, ((50 * i)/ width) * 50, ((50*i) % width) + 50, (((50 * i)/ width) * 50) + 50)
    c1 = cropped.crop (area)
    if isBit(c1) == True:
        binaryString += '1'
    else:
       binaryString += '0'    


str_data = ''

for i in range(0, len(binaryString), 7): 
      

    temp_data = int(binaryString[i:i + 7]) 
       

    decimal_data = BinaryToDecimal(temp_data) 
       

    str_data = str_data + chr(decimal_data)  
   
# printing the result 
print("The encoded message is: " + str_data) 


