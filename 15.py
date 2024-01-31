from PIL import Image
img=Image.open('tajmahal.jpg')
img.show()
width,height=img.size
pix=img.load()

for i in range(width):
        for j in range(height):
            r,g,b=pix[i,j]


            tr=(int)(0.393*r+0.769*b+0.189*b)
            tg=(int)(0.349*r+0.686*b+0.168*b)
            tb=(int)(0.272*r+0.534*b+0.131*b)

            pix[i,j]=(int(tr),int(tg),int(tb))

img.save('tajmahalthrishik.jpg')
img1=Image.open('tajmahalthrishik.jpg')
img1.show()
