n = int(input())

for i in range(0,n):
    for j in range(0,n):
        t = i*j
        if(i==0): print(j,end=' ')
        elif(j==0): print(i,end=' ')
        elif (j==i): print(t,end=' ')
        else: print(0,end=' ')
    print()