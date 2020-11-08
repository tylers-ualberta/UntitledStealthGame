import pygame
from engine import *
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
    player = Player(offset)
    enemy = Enemy(e_spawn1)
    cone = Cone(e_spawn1)

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
        wallB1 = Walls([0, 0], screen.get_width(), 10)
        wallB2 = Walls([0, 0], 10, screen.get_height())
        wallB3 = Walls([0, screen.get_height()-10], screen.get_width(), 10)
        wallB4 = Walls([screen.get_width()-10, 0], 10, screen.get_height())

        # Walls(corner(list), width, height, colour=(0,0,0))
        wall1 = Walls([0, 10], screen.get_width(), 100)
        wall2 = Walls([screen.get_width() - 100, 0], 100, screen.get_height())
        wall3 = Walls([0, screen.get_height()-100], screen.get_width(), 100)
        wall4 = Walls([0, screen.get_height()/2-100], 3*screen.get_width()/4, 200)

        # pygame.draw.rect(screen, (0, 0, 0), ((0, 10), (screen.get_width(), 100)))
        # pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width()-100, 0), (100, screen.get_height())))
        # pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()-100), (screen.get_width(), 100)))
        # pygame.draw.rect(screen, (0, 0, 0), ((0, screen.get_height()/2-100), (3*screen.get_width()/4, 200)))

        player.update_position()

        # Drawing
        screen.blit(player.surf, player.rect)
        screen.blit(enemy.surf, enemy.rect)
        screen.blit(cone.image, cone.rect)
        # wallB1.draw()
        screen.blit(wallB1.surf, wallB1.rect)
        # wallB2.draw()
        screen.blit(wallB2.surf, wallB2.rect)
        # wallB3.draw()
        screen.blit(wallB3.surf, wallB3.rect)
        # wallB4.draw()
        screen.blit(wallB4.surf, wallB4.rect)
        # wall1.draw()
        screen.blit(wall1.surf, wall1.rect)
        # wall2.draw()
        screen.blit(wall2.surf, wall2.rect)
        # wall3.draw()
        screen.blit(wall3.surf, wall3.rect)
        # wall4.draw()
        screen.blit(wall4.surf, wall4.rect)

        # Keep at bottom for display reasons
        pygame.display.flip()
        # Sets our framerate
        clock.tick(60)
        pass

    pygame.quit()

if __name__ == "__main__":
    run()