from PIL import Image

img=Image.open('messi.png')
img.show()

width,height=img.size
pix=img.load()

for i in range(width):
     for j in range(height):

         r,g,b=pix[i,j]
         gray=(r+g+b)/3
         pix[i,j]=(int (gray),int (gray),int(gray))

img.save("Grayedmessi.png")
img1=Image.open("Grayedmessi.png")
img1.show()         
