a,b = map(int,input().split())
n = int(input())
s=[]

for i in range(n):
    c,d= map(int,input().split())
    s.append(((((((c-a)**2) + ((d-b))**2))**0.5),c,d))

s.sort()

for i in s:
    print(i[1],i[2])


    

