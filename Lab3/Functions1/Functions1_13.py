import random
a = random.randint(1,20)
print('Hello! What is your name?')
name = input()
print('Well,',name,end=', I am thinking of a number between 1 and 20.\n')

print('Take a guess.')

def game(ans,nm,t):
    t+=1
    b=int(input())
    if(b==a):
        print('Good job,',nm,end='! You guessed my number in ')
        print(t,end=' guesses!')
    else: 
        if(b<a):
            print('Your guess is too low.')
            print('Take a guess.')
        else:
            print('Your guess is too higher.')
            print('Take a guess.')
        game(ans,nm,t)
game(a,name,0)
