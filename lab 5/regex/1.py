import re

def text(w):
    t=re.search("^a*b",w)
    if(t!=None):
        print('YES')
    else: print('NO')
m=input()
text(m)