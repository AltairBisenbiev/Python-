import re

m=input()
x = re.sub("_"," ",m)

x1 = re.split("\s", x)
for i in x1:
    print(i.capitalize(),end='')
