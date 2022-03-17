a='A'
for i in range(26):
    l = chr(ord(a)+i)
    s = ''+l+'.txt'
    open(s,'w')
    