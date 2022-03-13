import re

def text(w):
    t=re.search("[a-z]+_+[a-z]",w)
    if(t!=None):
        print('YES')
    else: print('NO')
m=input()
text(m)