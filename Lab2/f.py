s = int(input())
l = {}
cnt = 0
for i in range(s):
    a,b = map(str,input().split())
    l.setdefault(a,cnt)
    l[a]+=int(b)




mx = 0
for i in l.items():
    mx = max(mx,i[1])


asd = []


for i in l.items():
    if mx == i[1]:
        asd.append((i[0],"is lucky!"))
    else:
        asd.append((i[0],"has to receive",mx-i[1],"tenge"))

asd.sort()
for i in asd:
    print(*i)







    






