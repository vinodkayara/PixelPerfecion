from PIL import Image, ImageFilter
img=Image.open('tulip.jpg')
img.show()

img1=img.convert("L")
img1.save('tulipGrey.jpg')
img1.show()

img2=img1.filter(ImageFilter.Kernel((5,5),(0,0,-1,0,0,0,-1,-2,-1,0,-1,-2,16,-2,-1,0,-1,-2,-1,0,0,0,-1,0,0),1,0))
img2.save('tulipEdgeLoG.jpg')
img2.show()

