from PIL import Image
img=Image.open('messi.png')
img.show()

width,height=img.size
pix=img.load()

for i in range(width):
    for j in range(height):
        r,g,b=pix[i,j]
        pix[i,j]=(255-r,255-g,255-b)
img.save('NegMessi.png')
img1=Image.open('NegMessi.png')
img1.show()
