n = int(input())
y = 0
a=''
b=''
s=0
if(n%2==0):
    s=1
    y=0
    a+='#'
    b+='.'
else:
    s=0
    y=n
    a+='.'
    b+='#' 

for i in range(0,n):
    if(s==0): y-=1
    else: y+=1
    for j in range(0,n):
        if(j<y): print(a,end='')
        else: print(b,end='')
    print()