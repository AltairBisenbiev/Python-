def rec(arr,t):
    for i in arr:
        if(t<2):
            if(i==0): t+=1
        else:
            if(i==7):
                print(True)
                exit()
    return(False)

    
a = list(map(int,input().split()))

print(rec(a,0))

