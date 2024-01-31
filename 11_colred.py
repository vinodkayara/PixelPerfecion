from PIL import Image
import random

img=Image.open('messi.png')
img.show()

width=img
img.load()

width,height=img.size
pix=img.load()

for i in range(width):
     for j in range(height):

         r=random.randrange(0,255)
         g=random.randrange(0,255)
         b=random.randrange(0,255)

         pix[i,j]=(r,g,b)
         
img.save("colredmessi.png")
img1=Image.open("colredmessi.png")
img1.show()
         
