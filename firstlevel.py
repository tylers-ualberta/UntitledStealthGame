import pygame
pygame.init()

screen = pygame.display.set_mode([1710, 900])

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), ((150, 50), (50, 10)))  # ((posX, posY), (width (x), height (y)))
    # Position taken from top left corner, you provide the top left corner.
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (500, 10)))
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (10, 500)))
    pygame.draw.rect(screen, (0, 0, 0), ((0, 490), (500, 10)))
    pygame.draw.rect(screen, (0, 0, 0), ((490, 0), (10, 500)))


    pygame.display.flip()

pygame.quit()