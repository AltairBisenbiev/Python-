import random
from Functions1_13 import game

a = random.randint(1,20)
print('Hello! What is your name?')
name = input()
print('Well,',name,end=', I am thinking of a number between 1 and 20.\n')
print('Take a guess.')
game(a,name,0)
exit()