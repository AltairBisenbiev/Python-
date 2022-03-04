def Generator(n):
    for i in range(n):
        if i**2 <= n:
            yield i**2

N = int(input()) 
gen = Generator(N)
for i in gen:
    print(i)