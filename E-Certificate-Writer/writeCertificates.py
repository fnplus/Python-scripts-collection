import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import img2pdf
import os

def writeimage(template,font,size,coorx,coory,msg,rgb):
	image = Image.open(template)

	# initialise the drawing context with
	# the image object as background

	draw = ImageDraw.Draw(image)

	font = ImageFont.truetype(font, size=size)
	 
	# starting position of the message
	 
	(x, y) = (coorx, coory)
	message = msg
	color = rgb # black color
	 
	# draw the message on the background

	draw.text((x, y), message, fill=color, font=font)

	# save the edited image

	if image.mode == "RGBA":
		image = image.convert("RGB")

	image.save("./Output/"+msg+".png")


	with open("./Output/"+msg+".pdf","wb") as f:
		f.write(img2pdf.convert("./Output/"+msg+".png"))
	
	os.remove("./Output/"+msg+".png")

	image.close()

	f.close() 


#Accept User input for Required Details

print("Enter Certificate template Name: ", end="")
template=input()
print("Enter CSV Filename: ", end="")
filename=input()
print("Enter Column Name containing to Data: ", end="")
col=input()
print("Enter TrueType Font Filename: ", end="")
font=input()
print("Enter Font Size: ", end="")
size=int(input())
print("Enter Space Separated x,y Coordianates of text to written: ", end="")
coorx,coory=map(int,input().split())
print("Enter Space Separated RGB values of Text Color: ", end="")
r,g,b=map(str,input().split())


#Open CSV File
data=pd.read_csv(filename)

for row in data[col]: #Scan names row by row

	writeimage(template,font,size,coorx, coory,row,"rgb("+r+","+g+","+b+")")

