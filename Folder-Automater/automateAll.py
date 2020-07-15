import os 
import shutil 

os.chdir('/home/nopc/Downloads/SCRAP DOWNLOAD')

def move_pdf ():
    path_to_new_folder = os.getcwd() + '/PDFINHERE'
    for f in os.listdir():
        if f.endswith('.pdf'):
            current_file = os.getcwd() + '/'+ f
            shutil.move(current_file, path_to_new_folder)
            print("Success")

list_having_all_extensions = [] 
unique_extensions = []

def findall () :
    for f in os.listdir():
        ch = f.split('.')
        if len(ch) == 2:
            list_having_all_extensions.append(ch[1])
    removing_duplicates()    

def removing_duplicates ():
    unique_extensions = list(dict.fromkeys(list_having_all_extensions))
    print(unique_extensions)

def combining_all_pictures () :
    new_folder_path = os.getcwd() + '/Photos'
    #os.mkdir(new_folder_path)
    for f in os.listdir():
        ch = f.split('.')
        if ch[-1] == 'jpeg' or ch[-1] == 'png' or ch[-1] == 'jpg' or ch[-1] == 'obj'or ch[-1] == 'JPEG':
            current_file = os.getcwd() + '/'+ f
            shutil.move(current_file, new_folder_path)
            print("Success")

def combining_all_linux_and_windows_file () :
    new_folder_path = os.getcwd() + '/Linux_And_Temp_Executable_Files'
    #os.mkdir(new_folder_path)
    for f in os.listdir():
        ch = f.split('.')
        if ch[-1] == 'bin' or ch[-1] == 'deb' or ch[-1] == 'exe' or ch[-1] == 'zip' or ch[-1] == 'rpm' or ch[-1] == 'gz' or ch[-1] == 'xz':
                current_file = os.getcwd() + '/'+ f
                shutil.move(current_file, new_folder_path)
                print("Success")


def combining_all_ppts_and_doc () :
    new_folder_path = os.getcwd() + '/PPTS_AND_DOCS'
    #os.mkdir(new_folder_path)
    for f in os.listdir():
        ch = f.split('.')
        if len(ch) == 2:
            if ch[1] == 'doc' or ch[1] == 'odt' or ch[1] == 'ppt' or ch[1] == 'pptx':
                current_file = os.getcwd() + '/'+ f
                shutil.move(current_file, new_folder_path)
                print("Success")


findall()
move_pdf()
combining_all_pictures()
combining_all_linux_and_windows_file()
combining_all_ppts_and_doc()