import pygame
import sys
import Level_0
import Level_1

from pygame.locals import *
pygame.init()

Opening = True
background = (100,100,100)
red = (225,0,0)
black = (0,0,0)


screen = pygame.display.set_mode([1260, 700], HWSURFACE|DOUBLEBUF)
screen.fill(background)
pygame.display.flip()
FontWord = pygame.font.Font('freesansbold.ttf', 42)
Word = FontWord.render('Untitled Stealth Game', True, red, black)
BackRect = Word.get_rect()
StartWord = pygame.font.Font('freesansbold.ttf', 15)
Starting = StartWord.render('Press the Space Bar to Begin', True, (225,225,225), (100,100,100))
StartRect = Starting.get_rect()
StartRect.center = (630, 500)

BackRect.center = (630,200)
#Decor1 = pygame.image.load('Assets/PlayerWalking.png')

pygame.mixer.init()
try:
    pygame.mixer.music.load("Assets/widePutinSong.mp3")
    pygame.mixer.music.play()
except: pass


while Opening:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                Opening = False

    screen.blit(Word, BackRect)
    screen.blit(Starting, StartRect)


    pygame.display.flip()

Instructions = True
screen.fill(black)

InstructFont1 = pygame.font.Font('freesansbold.ttf', 42)
Instruct1 = InstructFont1.render('Use WASD to move', True, (225,225,225), black)
Instruct1Rect = Instruct1.get_rect()
Instruct1Rect.center = (630,500)
InstructFont2 = pygame.font.Font('freesansbold.ttf', 42)
Instruct2 = InstructFont2.render('Avoid the sight of the guards, indicated by the red cones', True, (225,225,225), black)
Instruct2Rect = Instruct2.get_rect()
Instruct2Rect.center = (630,400)
InstructFont3 = pygame.font.Font('freesansbold.ttf', 42)
Instruct3 = InstructFont1.render('Reach the flag to advance to the next level', True, (225,225,225), black)
Instruct3Rect = Instruct3.get_rect()
Instruct3Rect.center = (630,300)
while Instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                Instructions = False

    screen.blit(Instruct1, Instruct1Rect)
    screen.blit(Instruct2, Instruct2Rect)
    screen.blit(Instruct3, Instruct3Rect)
    pygame.display.flip()


cont1 = False
cont = Level_0.run()
if cont:
    cont1 = Level_1.run()
if cont1:
    screen = pygame.display.set_mode([1260, 700], HWSURFACE|DOUBLEBUF)
    Win = True
    WinFont = pygame.font.Font('freesansbold.ttf', 42)
    WinWords = WinFont.render('You Won!', True, (0,225,0), (225,225,225))
    WinRect = WinWords.get_rect()
    WinRect.center = (630,350)
    while Win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    Win = False
        screen.blit(WinWords, WinRect)
        pygame.display.flip()
else:
    screen = pygame.display.set_mode([1260, 700], HWSURFACE|DOUBLEBUF)
    Dead = True
    DeadFont = pygame.font.Font('freesansbold.ttf', 42)
    DeadWords = DeadFont.render('Game Over', True, (225,0,0), black)
    DeadRect = DeadWords.get_rect()
    DeadRect.center = (630,350)

    while Dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    Dead = False
        screen.fill(black)
        screen.blit(DeadWords, DeadRect)
        pygame.display.flip()


        

pygame.quit()

