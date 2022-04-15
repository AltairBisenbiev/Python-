from operator import le
import pygame
from pygame.locals import *
from pygame import mixer
import random
import sys
import time
pygame.init()
screen = pygame.display.set_mode((800,600))
FPS = pygame.time.Clock()
draw_on = False
last_pos = (0, 0)
a=[255,255,255,165,255,0,0,128,255,128,0]
b=[255,255,0,42,165,128,0,0,192,128,0]
c=[255,0,0,42,0,0,255,128,203,128,0]
cl = len(a)
t = 0
radius = 10
color = (255,255,255)
screen.fill((255,255,255))
t=1
font = pygame.font.SysFont('microsofttale',30)
try:
    while True:
        text = font.render("Press 1: Circle ", True, (0, 0, 0))
        text1 = font.render("Press 2: Rectangle ", True, (0, 0, 0))
        text2 = font.render("Press 3: Eraser ", True, (0, 0, 0))
        text3 = font.render("Press Space: Change Color ", True, (0, 0, 0))
        screen.blit(text,(70,10))
        screen.blit(text1,(70,30))
        screen.blit(text2,(70,50))
        screen.blit(text3,(70,70))
        
        e = pygame.event.wait()
        
        if e.type == pygame.QUIT:
            raise StopIteration
        if e.type == pygame.MOUSEBUTTONDOWN:
            
            if(t==1): pygame.draw.circle(screen, color, e.pos, radius)
            if(t==2): pygame.draw.rect(screen,color,(*e.pos,radius,radius))
            if(t==3): pygame.draw.rect(screen,(255,255,255),(*e.pos,radius,radius))
            

            draw_on = True
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                if(t==1):pygame.draw.circle(screen, color, e.pos, radius)
                if(t==2): pygame.draw.rect(screen,color,(*e.pos,radius,radius))
                if(t==3): pygame.draw.rect(screen,(255,255,255),(*e.pos,radius,radius))

                
            last_pos = e.pos
        pygame.display.flip()
        pygame.draw.rect(screen,color,(0,0,50,50))
        pygame.display.flip()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_1]:
            t=1
        if pressed_keys[pygame.K_2]:
            t=2
        if pressed_keys[pygame.K_3]:
            t=3
                
        if pressed_keys[pygame.K_SPACE]:
            if t<cl-1:
                t+=1
            else:
                t=0
        if pressed_keys[pygame.K_UP]:
            radius+=5
        if pressed_keys[pygame.K_DOWN]:
            radius-=5
        
        color = (a[t],b[t],c[t])
        pygame.display.update()
        FPS.tick(60)


            


except StopIteration:
    pass

pygame.quit()