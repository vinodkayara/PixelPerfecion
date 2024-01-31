from PIL import Image, ImageFilter
img=Image.open('tajmahal.jpg')
img.show()
img1=img.filter(ImageFilter.Kernel((3,3),(-1,-1,-1,-1,9,-1,-1,-1,-1),9,0))

img1.save('lbftajmahal.jpg')
img2=Image.open('lbftajmahal.jpg')
img2.show()
