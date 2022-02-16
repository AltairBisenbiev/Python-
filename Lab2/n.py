s = []
while True:
    n = int(input())
    if n == 0:
        break
    s.append(n)
l = []
for i in range(len(s)//2):
    l.append(s[0] + s[-1])
    s.pop(0)
    s.pop(-1)
    if(len(s) == 1):
        l.append(s[0])

for i in l:
    print(i,end=" ")

    
