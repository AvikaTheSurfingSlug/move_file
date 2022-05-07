import os
import shutil
from_dir = "C:/Users/Avika sama/Downloads/"
to_dir = "c:/Users/Avika sama/Downloads/stuff/School"
listoffiles = os.listdir(from_dir)
#print(listoffiles)
for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    #print(name)
    #print(extension)
    if extension == '':
        continue
    if extension in ['.txt','.docx','.doc','.pdf']:
        path1 = from_dir+'/'+filename
        path2 = to_dir+'/'+"School"
        path3 = to_dir+'/'+"School"+'/'+filename
        print(path1)
        print(path3)
        if os.path.exists(path2):
            print("moving..."+filename)
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("moving..."+filename)
            shutil.move(path1,path2)