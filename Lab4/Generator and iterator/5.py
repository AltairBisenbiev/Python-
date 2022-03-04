def Generator(n):
    for i in range(n,0,-1):
        yield i
N = int(input())
gen = Generator(N)
for i in gen:
    print(i,end=" ")