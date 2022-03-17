import os 
from os.path import isfile,join
a=os.getcwd()
dirlist= []
for root,directories,files in os.walk(a):
    for dir in directories:
        dirlist.append(join(root,dir))
for i in dirlist:
    print(i)
