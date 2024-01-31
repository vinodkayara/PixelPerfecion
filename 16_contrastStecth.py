from PIL import Image
img=Image.open('tulip.jpg')
img.show()

width,height=img.size
pix=img.load()
l=float(0.5)
m=2
n=float(0.5)

intenA=50
intenB=200


v=(l*intenA)
w=(m*(intenB+intenA)+v)

for i in range(width):
 for j in range(height):
               r,g,b=pix[i,j]

               if r>intenA:
                  r=(int)(l*r)
               elif r<=intenB:
                   r=(int)(m*(r-intenA)+v)
               else:
                    r=(int)(n*(r-intenB)+w)  


               if g>intenA:
                  g=(int)(l*g)
               elif g<=intenB:
                   g=(int)(m*(g-intenA)+v)

               else:
                    g=(int)(n*(g-intenB)+w)


               if b>intenA:
                  b=(int)(l*b)
               elif g<=intenB:
                   b=(int)(m*(b-intenA)+v)

               else:
                    b=(int)(n*(b-intenB)+w)


               if r>255:
                  r=255
               if g>255:
                  g=255
               if b>255:
                  b=255
               
                  
               pix[i,j]=r,g,b



             
  

img.save('tulipash.jpg')
img1=Image.open('tulipash.jpg')
img1.show()


                  
                   
                      
              
