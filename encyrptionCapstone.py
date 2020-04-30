#To use, on command line type python encytionCapstone fileName bigPicture smallPicture
#This program takes in a textFile, reads it, converts the string to binary data and pastes the small image on the bigger
#image based on every '1' it would read from the binary data. 

import binascii
import sys


filename = sys.argv[1]
with open(filename, 'rb') as f:
    content = f.read()
    
res = ''.join(format(ord(i), 'b') for i in content)

print('Text Encrypted') 

from PIL import Image

from PIL import Image 
  
# open the image 
Image1 = Image.open(sys.argv[2]) 
  
# make a copy the image so that the  
# original image does not get affected 
Image1copy = Image1.copy() 
Image2 = Image.open(sys.argv[3]) 
Image2copy = Image2.resize((50,50),resample=Image.BILINEAR)
 
# Resize smoothly down to 50*50 pixels

  
# paste image giving dimensions 
#Image1copy.paste(Image2copy, (0, 0))
#Image1copy.paste(Image2copy, (100,0))


out = Image1
width, height = Image1.size
for i in range(len(res)):
    if res[i] == "1":
        out.paste(Image2copy, ((50*i) % width , (((50 * i)/ width) * 50)) )

out.save('encryptedImage.jpg')
print('Encrypted Image saved')
 
