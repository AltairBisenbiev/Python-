n = int(input())
s = []
cnt = 0
for i in range(n):
    a = input().split()
    if a[0] == '1':
        s.append((a[1]))
    if a[0] == '2':
        cnt+=1
       

for i in range(cnt):
    print(s[i],end=" ")
        





