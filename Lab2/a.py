def jump(pos,s,arr,stat):

    stat[pos]=True
    if(len(arr)-1==pos):
        print(1)
        exit()
        
    else:
        for i in range(0,s):
            
            if pos+i+1<len(arr) and stat[pos+i+1]==False: 
                jump(pos+i+1,arr[pos+i+1],arr,stat)
            
    

array = list(map(int, input().split()))
status = []
for i in range(0,len(array)):
    status.append(False)
jump(0,array[0],array,status)  
print(0)