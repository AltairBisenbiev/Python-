from os import R_OK,X_OK,W_OK,F_OK,access
path = r"C:\Users\unnas\Desktop\pp2\Lab4\Generator and iterator\3.py"
if access(path,F_OK):
    print("It exists")
if access(path,R_OK):
    print("it's readable")
if access(path,W_OK):
    print("it's writable")
if access(path,X_OK):
    print("it's executable")
    