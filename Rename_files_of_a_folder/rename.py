import os
path = '/home/user_name/Desktop/newdata/wood' #path is given here
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'wood_'+str(i)+'.jpg'))
    i = i+1
