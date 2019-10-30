import os
from os.path import join

location = str(input("Directory Location : "))
extension =  str(input("Extension of files to search for : "))

for (dirname, dirs, files) in os.walk(location):
   for filename in files:
       if filename.endswith('.'+extension) :
           thefile = os.path.join(dirname,filename)
           print(os.path.getsize(thefile), thefile)