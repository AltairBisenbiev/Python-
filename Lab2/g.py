s = {}
n = int(input())
for i in range(n):
    a,b = map(str, input().split())
    s.setdefault(b,0)
    s[b] += 1
    

c = int(input())
for i in range(c):
    d,r,e = input().split()
    e = int(e)
    if r in s:
        s[r]-=e
        
ab = 0
for i in s.values():
    if i > 0:
        ab+=i

print("Demons left: " + str(ab) )



    



