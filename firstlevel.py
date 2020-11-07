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
        
        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            surface = pygame.display.set_mode((event.w, event.h),
                                              RESIZABLE|HWSURFACE|DOUBLEBUF)

    screen.fill((255, 255, 255))

    # ((posX, posY), (width (x), height (y)))
    # Position taken from top left corner, you provide the top left corner.
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (screen.get_width(), 10)))
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (10, screen.get_height())))
    pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()-10), (screen.get_width(), 10)))
    pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width()-10, 0), (10, screen.get_height())))
    player = pygame.draw.circle(screen, (0, 0, 255), (screen.get_width()-50, screen.get_height()-50), 10)

    pygame.display.flip()

pygame.quit()