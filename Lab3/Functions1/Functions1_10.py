def unique(arr,pos,pre):
    if(pos==len(arr)-1):
        exit()
    if(pos == 0):
        print(arr[pos],end=' ')
        pre=arr[pos]
        unique(arr,pos+1,pre)
    elif (arr[pos]!=pre):
        print(arr[pos],end=' ')
        pre=arr[pos]
        unique(arr,pos+1,pre)
    else: unique(arr,pos+1,pre)
        

a = list(map(int,input().split()))
unique(a,0,0)