from PIL import Image

img=Image.open('messi.png')
coordinates=x,y=100,50
print(img.getpixel(coordinates))
img.putpixel(coordinates,(0,0,0,255))
print(img.getpixel(coordinates))
