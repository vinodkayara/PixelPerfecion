from PIL import Image
img=Image.open('tulip.jpg')
img.show()

width,height=img.size
pix=img.load()

intenA=50
intenB=120

for i in range(width):
 for j in range(height):
     r,g,b = pix[i,j]


     if ((intenA<=r and r<=intenB) or (intenA<=g and g<=intenB) or (intenA<=b and b<=intenB)):
      r=g=b=225
     else:
      r=g=b=0
    

      pix[i,j]=(r,g,b)





             
  

img.save('lenakh.jpg')
img1=Image.open('lenakh.jpg')
img1.show()

    
     
