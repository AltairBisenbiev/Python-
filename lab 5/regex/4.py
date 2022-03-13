import re

def text(w):
    t=re.search("^[A-Z]+[a-z]",w)
    if(t!=None):
        print('YES')
    else: print('NO')
m=input()
text(m)
