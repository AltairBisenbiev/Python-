
def paln(word,i,nword):
    if i>=0:
     nword+=word[i]
     paln(word,i-1,nword)
    else: 
        if(word==nword):
            print(True)
            exit()
    
   
s = input()
e=''
paln(s,len(s)-1,e)
print(False)


