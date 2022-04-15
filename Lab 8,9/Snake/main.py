from operator import le
import pygame
from pygame.locals import *
from pygame import mixer
import random
import sys
import time
pygame.init()
FPS = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
snake = [1]
queuex = [400]
queuey = [400]
app = [0,0]
x=20
y=0
length = 1
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("body.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.center = (queuex[-1], queuey[-1])
    def draw(self, surface):
        for i in range(len(queuex)):
            x1 = queuex[i]
            y1 = queuey[i]
            surface.blit(self.image, (x1,y1)) 

    
t = 100
    
font = pygame.font.SysFont('microsofttale',32)
font1 = pygame.font.SysFont('microsofttale',46)
def creator(x, y,screen):
    lpl=str(lvl)
    creator_text = font.render("Snake lvl = "+lpl, True, (255, 255, 255)) 
    screen.blit(creator_text, (x, y))
    scr=str(length)
    score_text = font1.render("Score="+scr,True, (255,255,255))
    screen.blit(score_text, (x, y+30))
   
 
class apple(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.image = pygame.image.load('apple.png')
        self.image = pygame.transform.scale(self.image,(20,20))
        self.x = random.randint(5,35) * 20
        self.y = random.randint(5,35) * 20
        app[0]=self.x
        app[1]=self.y
        self.surface = screen
            
    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))

    def randompos(self):
        self.x = random.randint(5,35) * 20
        self.y = random.randint(5,35) * 20
        app[0]=self.x
        app[1]=self.y 
        


Run = True
sn = Snake()
ap = apple(screen)
all_sprites= pygame.sprite.Group()
all_sprites.add(sn)

dx=queuex[0]
dy=queuey[0]
fp = 10
wall = pygame.image.load('wall.png')
lvl = 1
while Run == True:
    text = font.render("Level: "+str(lvl), True, (255, 255, 255))
    text1 = font.render("Length: "+str(length), True, (255, 255, 255))
    text2 = font.render("Timer: "+str(t), True, (255, 255, 255))
    t-=1
    if(t==0):
        ap.randompos()
        t=100
    screen.fill((128,128,128))
    screen.blit(text,(30,30))
    screen.blit(text1,(30,50))
    screen.blit(text2,(30,70))
    if lvl > 0:
        for i in range(40):
          screen.blit(wall,(0,i*20)) 
          screen.blit(wall,(i*20,0)) 
          screen.blit(wall,(780,i*20)) 
          screen.blit(wall,(i*20,780)) 
    if lvl > 1:
        for i in range(13,27):
            screen.blit(wall,(13*20,i*20))
            screen.blit(wall,(27*20,i*20))
            if dx==13*20 and dy==i*20 or dx==27*20 and dy==i*20:
                pygame.quit() 
            if app[0]==13*20 and app[1]==i*20 or app[0]==27*20 and app[1]==i*20:
                ap.randompos()
    if lvl>2:
        for i in range(13,28):
            screen.blit(wall,(i*20,7*20))
            screen.blit(wall,(i*20,33*20))
            if dx==i*20 and dy==7*20 or dx==i*20 and dy==33*20:
                pygame.quit() 
            if app[0]==i*20 and app[1]==7*20 or app[0]==i*20 and app[1]==33*20:
                ap.randompos()

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if app[0]==queuex[-1] and app[1]==queuey[-1]:
        t = 100
        length+=1
        ap.randompos()
        fp+=0.3
    if (queuex[-1]==780 or queuey[-1]==800 or queuex[-1]==0 or queuey[-1]==0):
        pygame.quit()
    for i in range(len(queuex)-4):
        if(queuex[-1]==queuex[i] and queuey[-1]==queuey[i]):
            pygame.quit()  
    pressed_keys = pygame.key.get_pressed()
    if x==0 and pressed_keys[K_LEFT] and x==0:
        x=-20
        y=0
    if x==0 and pressed_keys[K_RIGHT] and x==0:
        x=20
        y=0

    if pressed_keys[K_UP] and y==0:
        y=-20
        x=0

    if pressed_keys[K_DOWN] and y==0:
        y=20
        x=0
    
    if length == 20:
        time.sleep(0.3)
        lvl+=1
        length=1
        dx==400
        dy==400
        fp=10
        ap.__init__
    else:
        dx+=x
        dy+=y
               
    ap.draw(screen)
    sn.draw(screen)
    queuex.append(dx)
    queuey.append(dy)
    queuex = queuex[-length:]
    queuey = queuey[-length:]
 


    pygame.display.update()
    FPS.tick(fp)
