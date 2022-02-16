def abc(t):
    if t==40:
        return(41)
    elif t == 41:
        return(40)
    elif t == 91:
        return(93)
    elif t == 93:
        return(91)
    elif t == 123:
        return(125)
    elif t == 125:
        return(123)
     
    
a = input()
arr = []
pr = []
for i in range(0,126):
    arr.append(0)
for i in a:

    b = ord(i)
    f = abc(b)
    arr[b]+=1
    if(b<f):
        pr.append(b)
        
    if(b>f ):
        if(arr[f]>0 and pr[-1]==f):
           
            arr[f]-=1
            arr[b]-=1
            pr.pop(-1)
sum = arr[40]+arr[41]+arr[91]+arr[93]+arr[123]+arr[125]

if sum == 0:
    print('Yes')
else:
    print('No')
