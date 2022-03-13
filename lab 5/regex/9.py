import re 

m=input()
x = re.findall("[A-Z][^A-Z]*",m)

for i in x:
    print(i,end=' ')
    
