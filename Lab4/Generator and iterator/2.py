def Generator(n):
    for i in range(n):
        if i%2==0 and i!=0:
            yield i
            

N = int(input()) 
gen = Generator(N)
j=0
for i in gen:
    if j==0:
        print(i,end="")
        j+=1
    else:
        print(",",i,end="")
   
    