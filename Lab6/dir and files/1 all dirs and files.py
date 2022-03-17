import os 
from os.path import isfile,join
a=os.getcwd()
filelist=[]


for root,dirs,files in os.walk(a):
    for file in files:
        filelist.append(join(root,file))
for i in filelist:
    print(i)

dirlist= []
for root,directories,files in os.walk(a):
    for dir in directories:
        dirlist.append(join(root,dir))
for i in dirlist:
    print(i)
