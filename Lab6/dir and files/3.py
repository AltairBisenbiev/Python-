from os import R_OK,X_OK,W_OK,F_OK,access
from os.path import basename
a = input()
if access(a,F_OK):
    print(basename(a))
    print(a)
