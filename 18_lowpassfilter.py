from PIL import Image, ImageFilter
img=Image.open('tulip.jpg')
img.show()
img1=img.filter(ImageFilter.Kernel((3,3),(1,1,1,1,1,1,1,1,1),9,0))

img1.save('LPFtulip.jpg')
img2=Image.open('LPFtulip.jpg')
img2.show()
