from PIL import Image, ImageFilter
img=Image.open('tulip.jpg')
img.show()

img1=img.convert("L")
img1.save('tulipGrey.jpg')
img1.show()

img2=img1.filter(ImageFilter.Kernel((3,3),(-2,-2,0,-2,0,2,0,2,2),1,0))
img2.save('tulipEdgeLoGsobel.jpg')
img2.show()

