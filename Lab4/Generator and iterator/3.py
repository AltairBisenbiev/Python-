def Generator(n):
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i
            

N = int(input()) 
gen = Generator(N)
for i in gen:
    print(i,end=" ")
    