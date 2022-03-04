def solve(numheads, numlegs):
    for i in range(0,numheads):
        t = i+1
        c=t*2
     
        r =((numlegs-(t*2))/4)
     
        if (((numlegs-(t*2))%4)==0 and  t+r==35):
           
            print("Chickens: ",t)
            print("Rabbits: ", r)
a,b = map(int,input().split())
solve(a,b)

