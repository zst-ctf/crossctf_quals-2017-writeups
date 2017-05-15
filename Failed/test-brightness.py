'''
with open("test.png", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

chararr = map(lambda x: chr(x), b)
print ''.join(chararr)
print ','.join(map(lambda x: str(x), b)
)

'''
# http://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil


import binascii
def bin2ascii(input):
    n = int(input, 2)
    return chr(n)
    #return binascii.unhexlify('%x' % n)
import sys
from PIL import Image
im = Image.open('output.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
#print pixel_values
for i, pix in enumerate(pixel_values):
	if pix == 255:
		sys.stdout.write('1')
	else:
		sys.stdout.write('0')
