from PIL import Image, ImageFilter
img=Image.open('mandrill.jpg')
img.show()

kernel_Orig=[
    [-1,2,-1],
    [2,2,2],
    [-1,2,-1]
    ]
kernel= [list(reversed(row)) for row in reversed(kernel_Orig)]

for row in kernel:
    print (row)

flattened_kernel=[element for row in kernel for element in row]
print(flattened_kernel)


img1=img.filter(ImageFilter.Kernel((3,3),flattened_kernel,1,0))

img1.save('mandrill1.jpg')
img1.show()
