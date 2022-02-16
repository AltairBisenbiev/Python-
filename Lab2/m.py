s = []
while True:
    a = input().split()

    if a[0] == '0':
        break

    s.append((a[2],a[1],a[0]))

s.sort()
f=[]

for i in s:
    f.append((i[2],i[1],i[0]))

for i in f:
    print(*i)
    

