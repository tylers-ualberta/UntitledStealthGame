import pygame
from engine import *
from pygame.locals import *

""" Provide the necessary info for the main game to be able to generate the
level.

Level: 0

Description: Tutorial level

"""

pygame.init()
end = False
# Main function that runs
def run():

    screen = pygame.display.set_mode([1260, 700], RESIZABLE|HWSURFACE|DOUBLEBUF)
    running = True

    # Entity spawn conditions
    # offset indicates player spawn point
    offset = [30, screen.get_height()-180]
    # Set enemy spawn
    e_spawn1 = [3*screen.get_width()/4+20, screen.get_height()/2-10]
    # Set goal location
    goal = [50, screen.get_height()/5+20]

    # Initializing players and enemies
    player = Player(offset, sprite="Assets/Player.png")
    enemy = Enemy(e_spawn1, sprite="Assets/SecurityGuard.png")
    cone = Cone(e_spawn1, orientation="r")
    endflag = Item(goal, sprite="Assets/EndFlag.png")

    start_ticks = pygame.time.get_ticks() #starter tick

    # Initialize Cone State
    cone_state = 0

    # Start clock for clock.tick
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
        wall2 = Walls([screen.get_width() - 115, 0], 115, screen.get_height())
        wall3 = Walls([0, screen.get_height()-100], screen.get_width(), 100)
        wall4 = Walls([0, screen.get_height()/2-100], 3*screen.get_width()/4+10, 200)

        player.update_position()

        # Calculates time
        time = (pygame.time.get_ticks() - start_ticks) / 1000 #calculate how many seconds
        # Change view cone
        if time > 2:
            start_ticks = pygame.time.get_ticks()
        
            if cone_state > 3:
                cone_state = 0
            if cone_state == 0:
                cone.kill()
                cone = Cone([3*screen.get_width()/4+20, screen.get_height()/2-10], orientation="d")
            elif cone_state == 1:
                cone.kill()
                cone = Cone([3*screen.get_width()/4+20, screen.get_height()/2-10], orientation="r")
            elif cone_state == 2:
                cone.kill()
                cone = Cone([3*screen.get_width()/4+20, screen.get_height()/2-10], orientation="u")
            elif cone_state == 3:
                cone.kill()
                cone = Cone([3*screen.get_width()/4+20, screen.get_height()/2-10], orientation="r")
            cone_state += 1

        # Drawing
        screen.blit(player.image, player.rect)
        screen.blit(enemy.image, enemy.rect)
        screen.blit(cone.image, cone.rect)
        screen.blit(endflag.image, endflag.rect)

        # Walls
        screen.blit(wallB1.surf, wallB1.rect)
        screen.blit(wallB2.surf, wallB2.rect)
        screen.blit(wallB3.surf, wallB3.rect)
        screen.blit(wallB4.surf, wallB4.rect)
        screen.blit(wall1.surf, wall1.rect)
        screen.blit(wall2.surf, wall2.rect)
        screen.blit(wall3.surf, wall3.rect)
        screen.blit(wall4.surf, wall4.rect)
        
        # Keep at bottom for display reasons
        pygame.display.flip()
        
        # Initialize frame rate
        clock.tick(60)
    return end



if __name__ == "__main__":
    run()
    pygame.quit()
