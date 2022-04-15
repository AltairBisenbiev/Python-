import pygame
from pygame.locals import *
from pygame import mixer
import random
import sys
import time


pygame.display.set_caption("Racer")
#Time
FPS = pygame.time.Clock()
score = 0
# Initializing pygame
pygame.init()
bkgr = pygame.image.load('street.png')
# Creating screen
screen = pygame.display.set_mode((800, 800))
positions = [100,270,450,640]
posit = [0,0,0,0]
speed = 5
font = pygame.font.SysFont('microsofttale',32)
font1 = pygame.font.SysFont('microsofttale',46)
#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pl1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.image = pygame.transform.scale(self.image, (100,200))
    
    def move(self):
        global speed
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 50:
            if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-7, 0)  
                       
              
        if self.rect.right<700:
            if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(7, 0)
                  
        if self.rect.top >50:
            if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -7) 
                       
              
        if self.rect.bottom<700:
            if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, 7)
                  
                  

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pl2.png")
        self.rect = self.image.get_rect()
        i = random.randint(0,3)

        self.rect.center=(positions[i],-200) 

        
        self.image = pygame.transform.scale(self.image, (100,200))
 
      def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.top > 750):
           self.rect.top = 0
           self.rect.center = (positions[random.randint(0,3)], -200)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
class Coin (pygame.sprite.Sprite):
      def __init__(self):
        global score
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        i = random.randint(0,3)

        self.rect.center=(positions[i],0) 
    
        
        self.image = pygame.transform.scale(self.image, (100,100))
 
      def move(self):
        self.rect.move_ip(0,6)
        if (self.rect.top > 750):
           self.rect.top = 0
           self.rect.center = (positions[random.randint(0,3)], 0)
  
 
# Loading playlist for interesting game
music_list = 'music1.wav'
music = pygame.mixer.music.load(music_list)
pygame.mixer.music.play(-1)
# Font   
a = 0

#Game
    

# Functions for text
def creator(x, y):
    creator_text = font.render("Race or Lose", True, (0, 0, 0)) 
    screen.blit(creator_text, (x, y))
    scr=str(score)
    score_text = font1.render("Score="+scr,True, (0,0,0))
    screen.blit(score_text, (x, y+30))
   

    



#Objects
Car = Player()
Car1 = Enemy()


coin = Coin()
enemies = pygame.sprite.Group()
enemies.add(Car1)


all_sprites = pygame.sprite.Group()
all_sprites.add(Car)
all_sprites.add(Car1)

all_sprites.add(coin)
coins = pygame.sprite.Group()
coins.add(coin)
running = True
t=0
u = 0
while running:
    if score%3==0 and score!=0:
        u=1
        score+=1
    if u==1:
        speed+=1
        u=0
    screen.blit(bkgr, (0, 0))
    creator(350, 0)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    for entity in all_sprites:
        t+=1
        screen.blit(entity.image, entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(Car, coins): 
        score+=1
        coin.__init__()
        pygame.display.update()
        
        
        
        
        
            
        
        
        
    if pygame.sprite.spritecollideany(Car, enemies):
          pygame.display.update()
          for entity in all_sprites:
             entity.kill() 
          pygame.quit()
          time.sleep(2)
               
        
       

    
    pygame.display.update()
    FPS.tick(60)
    