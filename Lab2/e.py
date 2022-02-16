nandx = list(input().split())
if(len(nandx)==1):
    s=int(input())
    nandx.append(s)

n = int(nandx[0])
x = int(nandx[1])
xr = 0
arr=[]

for i in range(0,n):

    arr.append(x+i*2)
    if(i>0):
        xr^=arr[i]
    else:xr=arr[i]  
print(xr)