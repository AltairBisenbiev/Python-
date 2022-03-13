import re

def text(w):
    t=re.search("ab{2,3}",w)
    if(t!=None):
        print('YES')
    else: print('NO')
m=input()
text(m)