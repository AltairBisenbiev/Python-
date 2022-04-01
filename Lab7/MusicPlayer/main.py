import pygame
from pygame import mixer

# Initializing pygame
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 16)

# Creating screen
screen = pygame.display.set_mode((800, 600))

# Loading playlist
music_list = ['music1.wav', 'music2.wav', 'music3.wav']
a = 0


# Functions for text
def creator(x, y):
    creator_text = font.render("Playlist of Altair", True, (0, 0, 0))
    screen.blit(creator_text, (x, y))


def guide(x, y):
    text = ("Space for start from beginning; P to pause; C to continue; Right/Left Arrow for next/prev")

    guide_text = font.render(text, True, (0, 0, 0))

    screen.blit(guide_text, (x, y))


def currentmusic1(x, y):
    music_one_name = font.render("Tokio Drift", True, (0, 0, 0))

    screen.blit(music_one_name, (x, y))


def currentmusic2(x, y):
    music_two_name = font.render("Baby Mama", True, (0, 0, 0))

    screen.blit(music_two_name, (x, y))


def currentmusic3(x, y):
    music_two_name = font.render("Immigrant song", True, (0, 0, 0))

    screen.blit(music_two_name, (x, y))


# MusicPlayer Loop
running = True
while running:
    screen.fill((0, 128, 0))
    screen.blit(screen, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mixer.music.load(music_list[a])
                mixer.music.play()
                mixer.music.queue(music_list[a + 1])
                mixer.music.queue(music_list[a + 2])

            if event.key == pygame.K_p:
                mixer.music.pause()

            if event.key == pygame.K_c:
                mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                mixer.music.stop()
                if a < len(music_list) - 1:
                    mixer.music.load(music_list[a + 1])
                    mixer.music.play()
                    a += 1
                else:
                    a = 0

                    mixer.music.load(music_list[a])
                    mixer.music.play()

            if event.key == pygame.K_LEFT:
                mixer.music.stop()
                if a > 0:
                    mixer.music.load(music_list[a - 1])
                    mixer.music.play()
                    a -= 1
                elif a == 0:
                    mixer.music.load(music_list[len(music_list) - 1])
                    mixer.music.play()
                    a = len(music_list) - 1

        # if mixer.music.get_busy()

    creator(10, 560)
    guide(60, 520)
    if a == 0:
        currentmusic1(60, 400)

    if a == 1:
        currentmusic2(60, 400)

    if a == 2:
        currentmusic3(60, 400)

    pygame.display.flip()
