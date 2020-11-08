# Please include the following code in every level file.
import pygame
from pygame.locals import *
from engine import *  # Allows you to call engine classes without the engine.class notation
pygame.init()

# Set your offset variable above this, remeber it is from the bottom right.
player = Player(offset)
screen = pygame.display.set_mode([1260, 700], RESIZABLE|HWSURFACE|DOUBLEBUF)
running = True
clock = pygame.time.Clock()
while running:

    # Handles quitting the game, resizing the window
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
    # Sets screen colour
    screen.fill((255, 255, 255))
    # Draws boarder walls
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (screen.get_width(), 10)))
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (10, screen.get_height())))
    pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()-10), (screen.get_width(), 10)))
    pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width()-10, 0), (10, screen.get_height())))
    # Updates player's position each loop
    player.update_position()
    player.draw()
    pygame.display.flip()

    # Sets our framerate
    clock.tick(60)