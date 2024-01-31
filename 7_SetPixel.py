from PIL import Image

img=Image.open('messi.png')
pix=img.load()
print(pix[100,50])

pix[100,50]=(0,0,0)
print(pix[100,50])
img.show()
