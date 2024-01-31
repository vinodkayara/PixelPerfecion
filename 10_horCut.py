from PIL import Image

img = Image.open("messi.png")
img.show()

width,height = img.size
newHeight= int(height/2)

for x in range(height):
        img.putpixel((x,newHeight),(10,10,10,255))

img.save("nhmessi.png")
img1 = Image.open("nhmessi.png")
img1.show()
