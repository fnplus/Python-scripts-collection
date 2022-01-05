from PIL import Image
import os
#current format the image is in
img=Image.open('imagename.jpg')
#desirable format
img.save('imagename.png')