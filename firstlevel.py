import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([500, 500], RESIZABLE|HWSURFACE|DOUBLEBUF)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), ((150, 50), (50, 10)))  # ((posX, posY), (width (x), height (y)))
    # Position taken from top left corner, you provide the top left corner.
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (screen.get_width(), 10)))
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (10, screen.get_height())))
    pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()-10), (screen.get_width(), 10)))
    pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width()-10, 0), (10, screen.get_height())))


    pygame.display.flip()

pygame.quit()