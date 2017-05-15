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

from PIL import Image
im = Image.open('picaso.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
#print pixel_values
dict = {
}
for i, pix in enumerate(pixel_values):
    try:
        dict[pix] += 1
    except KeyError:
        dict[pix] = 1

print dict