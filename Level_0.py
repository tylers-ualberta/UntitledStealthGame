import pygame
import engine
from pygame.locals import *
pygame.init()
""" Provide the necessary info for the main game to be able to generate the
level.

Level: 0

Description: Tutorial level

NOTES:
Bottom right is 1260 x 700
"""
# offset indicates player spawn point
offset = [50, 50]

class walls():

    pass



def main():
    player = engine.player(offset)
    screen = pygame.display.set_mode([1260, 700], RESIZABLE|HWSURFACE|DOUBLEBUF)
    running = True


    clock = pygame.time.Clock()
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
                player.resize()
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (screen.get_width(), 10)))
        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (10, screen.get_height())))
        pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()-10), (screen.get_width(), 10)))
        pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width()-10, 0), (10, screen.get_height())))
        player.update_position()
        player.draw()
        pygame.display.flip()

        # Sets our framerate
        clock.tick(60)
        pass

pygame.quit()