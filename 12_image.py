from PIL import Image

img=Image.open('messi.png')
img.show()

width,height=img.size
pix=img.load()

for i in range(width):
     for j in range(height):

         r,g,b=pix[i,j]
         pix[i,j]=(0,0,b)

img.save("Redmessi.png")
img1=Image.open("Redmessi.png")
img1.show()         
