from PIL import Image

img = Image.open("messi.png")
img.show()

width,height = img.size
newWidth= int(height2)

for x in range(height):
        img.putpixel((newWidth,x),(10,10,10,255))

img.save("nmessi.png")
img1 = Image.open("nmessi.png")
img1.show()
