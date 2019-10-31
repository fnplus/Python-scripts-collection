import sys
import cv2
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(sys.path[0]) if isfile(join(sys.path[0], f))]
print(onlyfiles)
length = int(input("Enter the length of the image : "))
breadth = int(input("Enter the breadth of the image : "))
a=0
for files in onlyfiles:
    a +=1
    if( '.jpg' in files or '.jpeg' in files or '.png' in files): #Add more fomats here if you want 
        image = cv2.imread(files,1)
        resized = cv2.resize(image,(length,breadth))
        cv2.imwrite(files,resized)
        print(resized.shape)
print(a," files were updated!")