def histog(a):
    
    for i in a:
        b=''
        for j in range(0,i):
            b+='*'
        print(b)
arr=list(map(int,input().split()))
histog(arr)
