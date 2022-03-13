import re

m=input()
x = re.findall("[a-z]|[A-Z]",m)

for i in x:
    print(i.capitalize() ,end=' ')
    
