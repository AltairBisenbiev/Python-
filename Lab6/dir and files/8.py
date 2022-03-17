from os import remove,access,F_OK,X_OK
from os.path import basename
a = r"C:\Users\unnas\Desktop\pp2\file.txt"
t = basename(a)
if(access(a,X_OK) and access(a,F_OK)):
    print('True') 
else: print('False')
remove(t)