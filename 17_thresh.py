from PIL import Image
img=Image.open('lena.jpg')
img.show()

width,height=img.size
pix=img.load()

thresh=80

for i in range(width):
 for j in range(height):
     r,g,b = pix[i,j]

     avg=(r+g+b)/3

    
    
     if avg>thresh:
         pix[i,j]=(255,255,255)
     else:
        pix[i,j]=(0,0,0)


        pix[i,j]=r,g,b



             
  

img.save('lenaash.jpg')
img1=Image.open('lenaash.jpg')
img1.show()
