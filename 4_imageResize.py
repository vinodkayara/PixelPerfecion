from PIL import Image
img=Image.open('tajmahal.jpg')
img.show()

newSize=(427,240)
img1=img.resize(newSize)

img1.save('NewSizeTaj.jpg')
img1=Image.resize('NewSizeTaj.jpg')
img1.show()
