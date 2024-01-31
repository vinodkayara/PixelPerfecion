from PIL import Image

img=Image.open('tajmahal.jpg')

pix=img.load()

print(pix[100,50])
