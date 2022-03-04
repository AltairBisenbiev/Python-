
def reverse(sen,ln):
    
    if(ln==-1):
       exit()
    else:
        print(sen[ln],end=' ')
        ln-=1
        reverse(sen,ln)

a = list(map(str,input().split()))
ans = ''
reverse(a,len(a)-1)
