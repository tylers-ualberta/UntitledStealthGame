import pygame
import engine
from pygame.locals import *

""" Provide the necessary info for the main game to be able to generate the
level.

Level: 0

Description: Tutorial level

"""

# Main function that runs
def run():
    pygame.init()

    screen = pygame.display.set_mode([1260, 700], RESIZABLE|HWSURFACE|DOUBLEBUF)
    running = True

    # Entity spawn conditions
    # offset indicates player spawn point
    offset = [30, screen.get_height()-180]
    # Set enemy spawn
    e_spawn1 = [3*screen.get_width()/4+20, screen.get_height()/2-10]

    # Initializing players and enemies
    player = engine.Player(offset)
    enemy = engine.Enemy(e_spawn1)

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

        # Boundary rectangles
        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (screen.get_width(), 10)))
        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (10, screen.get_height())))
        pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()-10), (screen.get_width(), 10)))
        pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width()-10, 0), (10, screen.get_height())))

        # Walls
        # pygame.draw.rect(screen, colour, (top-left, (width,height))
        pygame.draw.rect(screen, (0, 0, 0), ((0, 10), (screen.get_width(), 100)))
        pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width()-100, 0), (100, screen.get_height())))
        pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()-100), (screen.get_width(), 100)))
        pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()/2-100), (3*screen.get_width()/4, 200)))

        player.update_position()
        # DELETE, replace with player.image, keep in classes
        screen.blit(player.surf, player.rect)
        # DELETE, replace with enemy.image, keep in classes
        screen.blit(enemy.surf, enemy.rect)

        # Keep at bottom for display reasons
        pygame.display.flip()
        # Sets our framerate
        clock.tick(60)
        pass

    pygame.quit()

if __name__ == "__main__":
    run()