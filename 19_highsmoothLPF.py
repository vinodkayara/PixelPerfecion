from PIL import Image, ImageFilter
img=Image.open('tajmahal.jpg')
img.show()
img1=img.filter(ImageFilter.Kernel((5,5),(1,1,1,1,1,1,5,5,5,1,1,5,44,5,1,1,5,5,5,1,1,1,1,1,1),100,0))

img1.save('lbftajmahal.jpg')
img2=Image.open('lbftajmahal.jpg')
img2.show()
