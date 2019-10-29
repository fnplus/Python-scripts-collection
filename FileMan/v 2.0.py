

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:23:10 2019
@author: arghac14
"""


import os
import time
from pathlib import Path

def createDir(BASE_DIR,dn):
  for i in range(dn):
    os.mkdir(BASE_DIR + str(i) + 'Folder')
    
def createFile(BASE_DIR,fn):
  for i in range(fn):
    f=open(BASE_DIR + str(i) + 'File.txt','w')
    f.close()

def fileCounter(BASE_DIR):
  fileCount = 0
  dirCount = 0

  for root, dirs, files in os.walk(BASE_DIR):
    print('Looking in:',root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

  print('Number of files: ',fileCount)
  print('Number of Directories: ',dirCount)
  print('Total: ',(dirCount + fileCount))

def searchFile(BASE_DIR,ss):
  
  for root, dirs, files in os.walk(BASE_DIR):
    print('Looking in:',root)
    for Files in files:
      
      try:
        found = Files.find(ss)
        if found != -1:
          print(ss, 'Found!')
          break
        elif found == -1:
            print("File not fount!")
        else:
            print("Something went wrong!")
      except:
        print('Something went wrong! Try again..')
        exit()
      




def organize():
    DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

    }


    FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

    try:
        os.mkdir("OTHER-FILES")
    except:
        pass

    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER-FILES/' + str(Path(dir)))
        except:
            pass


if __name__ =='__main__':
  #BASE_DIR ='C:/Users/User/Desktop/fileman/'
  BASE_DIR=input("Enter the absolute path of the location where the operations are going to take place [eg: C:/Users/User/Desktop/fileman/ ] :  ")
  print("|| 1.Create Directories | 2.Create Files | 3.Organize Files | 4.Count Files & Directories | 5. Search files ||")
  op=int(input("Choose an option: "))
  if(op==1):
    dn=int(input("How many directories you want to create? : "))
    createDir(BASE_DIR,dn)
    time.sleep(2)
    print("Process completed!")
  elif(op==2):
    fn=int(input("How many files you want to create? : "))
    createFile(BASE_DIR,fn)
    time.sleep(2)
    print("Process completed!")
  elif(op==3):
    organize()
    time.sleep(2)
    print("Done")
  elif(op==4):
    fileCounter(BASE_DIR)
  elif(op==5):
    ss=input("Enter the exact file name with extenstion: ")
    searchFile(BASE_DIR,ss)
  else:
    print("Invalid Option!")
