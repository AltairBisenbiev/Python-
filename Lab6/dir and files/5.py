from os import R_OK,X_OK,W_OK,F_OK,access
from os.path import basename
a = __file__
file = open(a,"r")
text=file.read()
mylist = text.split("\n")

with open('file.txt', 'w') as x:
    for i in mylist:
        x.write("%s\n" % i)