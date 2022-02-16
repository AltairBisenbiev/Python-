n = int(input())
a,b,c = 0,0,0
s = []
cnt = 0
for i in range(n):
    l = input()
    for i in l:
        if ord(i) >= 65 and ord(i) <= 90:
            a+=1
        if ord(i) >= 97 and ord(i) <= 122:
            b+=1
        if ord(i) >=48 and ord(i) <= 57:
            c+=1
    
    if a!=0 and b!=0 and c!=0:
        s.append(l)

    a,b,c = 0,0,0

s.sort()

j = {}
for i in s:
    j.setdefault(i)
for i in j:
    cnt+=1
print(cnt)
for i in j:
    print(i)


            

