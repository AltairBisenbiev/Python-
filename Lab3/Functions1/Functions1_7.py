def three(arr):
    j = 0
    for i in arr:
        
        if(j==0):
            pr=i
        elif(pr==i and pr==3):
            print(True)
            exit()
        j+=1
        pr=i
    return(False)
            
        
        

a = list(map(int,input().split()))
print(three(a))