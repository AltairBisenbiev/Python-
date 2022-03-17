a = input()
u=0
l=0
for i in a:
    if(i.isupper()): 
        u+=1
    if(i.islower()):
        l+=1
print("Upper cases:",u)
print("Lower cases:",l)
