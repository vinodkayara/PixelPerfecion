from PIL import Image

img=Image.open('messi.png')
coordinates=x, y=100, 50
print(img.getpixel(coordinates))
