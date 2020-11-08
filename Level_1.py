import pygame
from engine import *
from pygame.locals import *

""" Provide the necessary info for the main game to be able to generate the
level.

Level: 1

Description: Intro to timing.

"""

pygame.init()
# Main function that runs
def run():

    screen = pygame.display.set_mode([1260, 700], RESIZABLE|HWSURFACE|DOUBLEBUF)
    running = True

    # Add all sprites to their appropriate sprite group(s). Any sprites from the
    # assests folder need to be in all_sprites_img.
    all_sprites_surf = pygame.sprite.Group()
    all_sprites_img = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    items = pygame.sprite.Group()
    cone_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    wallB1 = Walls([0, 0], screen.get_width(), 10)
    wallB2 = Walls([0, 0], 10, screen.get_height())
    wallB3 = Walls([0, screen.get_height()-10], screen.get_width(), 10)
    wallB4 = Walls([screen.get_width()-10, 0], 10, screen.get_height())
    all_sprites_surf.add(wallB1)
    all_sprites_surf.add(wallB2)
    all_sprites_surf.add(wallB3)
    all_sprites_surf.add(wallB4)
    wall_sprites.add(wallB1)
    wall_sprites.add(wallB2)
    wall_sprites.add(wallB3)
    wall_sprites.add(wallB4)

    # Entity spawn conditions
    # offset indicates player spawn point
    offset = [120, screen.get_height()-120]
    # Set enemy spawn
    e_spawn1 = [300, 510]
    e_spawn2 = [850, 650]
    e_spawn3 = [1100, 350]
    e_spawn4 = [730, 350]
    e_spawn5 = [400, 330]
    e_spawn6 = [605, 100]
    e_spawn7 = [1000, 180]
    # Set goal location
    goal = [50, screen.get_height()/5+20]

    # Initializing players and enemies
    player = Player(offset, sprite="Assets/Player.png")
    enemy1 = Enemy(e_spawn1, sprite="Assets/SecurityGuard.png")
    enemy2 = Enemy(e_spawn2, sprite="Assets/SecurityGuard.png")
    enemy3 = Enemy(e_spawn3, sprite="Assets/SecurityGuard.png")
    enemy4 = Enemy(e_spawn4, sprite="Assets/SecurityGuard.png")
    enemy5 = MovingEnemy(e_spawn5, [(100, 250), (520, 420)], speed=10, sprite="Assets/SecurityGuard.png")
    enemy6 = Enemy(e_spawn6, sprite="Assets/SecurityGuard.png")
    enemy7 = MovingEnemy(e_spawn7, [(1000, 180), (200, 30)], speed=10, sprite="Assets/SecurityGuard.png")
    cone1 = Cone(e_spawn1, orientation="d")
    cone2 = Cone(e_spawn2, orientation="u")
    cone3 = Cone(e_spawn3, orientation="u")
    cone4 = Cone(e_spawn4, orientation="d")
    cone6 = Cone(e_spawn6, orientation="l")
    endflag = Item(goal, sprite="Assets/EndFlag.png")

    start_ticks = pygame.time.get_ticks() #starter tick

    # Initialize Cone State
    cone1_state = 0
    cone2_state = 0
    cone3_state = 0
    cone4_state = 0
    cone6_state = 0

    # Start clock for clock.tick
    clock = pygame.time.Clock()

    while running:
        # Handles quitting the game, resizing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        screen.fill((255, 255, 255))

        # Walls(corner(list), width, height, colour=(0,0,0))
        wall1 = Walls([0, screen.get_height()/3], 50, 10)
        wall2 = Walls([150, screen.get_height()/3], screen.get_width()-150, 10)
        wall3 = Walls([0, 2*screen.get_height()/3], screen.get_width()-200, 10)
        wall4 = Walls([screen.get_width()/5, 2*screen.get_height()/3], 10, 100)
        wall5 = Walls([screen.get_width()/3, 5*screen.get_height()/6], 250, 10)
        wall6 = Walls([2*screen.get_width()/3, screen.get_height()-100], 10, 100)
        wall7 = Walls([2*screen.get_width()/3, screen.get_height()/3], 10, 150)
        wall8 = Walls([screen.get_width()/2, screen.get_height()/3], 10, 40)
        wall9 = Walls([screen.get_width()/2, screen.get_height()/2], 10, 120)

        # Add entities to sprite group
        all_sprites_img.add(player)
        all_sprites_img.add(enemy1)
        enemies.add(enemy1)
        all_sprites_img.add(enemy2)
        enemies.add(enemy2)
        all_sprites_img.add(enemy3)
        enemies.add(enemy3)
        all_sprites_img.add(enemy4)
        enemies.add(enemy4)
        all_sprites_img.add(enemy5)
        enemies.add(enemy5)
        all_sprites_img.add(enemy6)
        enemies.add(enemy6)
        all_sprites_img.add(enemy7)
        enemies.add(enemy7)
        all_sprites_img.add(endflag)
        items.add(endflag)
        cone_sprites.add(cone1)
        cone_sprites.add(cone2)
        cone_sprites.add(cone3)
        cone_sprites.add(cone4)
        cone_sprites.add(cone6)

        # Add walls to sprite group
        all_sprites_surf.add(wall1)
        all_sprites_surf.add(wall2)
        all_sprites_surf.add(wall3)
        all_sprites_surf.add(wall4)
        all_sprites_surf.add(wall5)
        all_sprites_surf.add(wall6)
        all_sprites_surf.add(wall7)
        all_sprites_surf.add(wall8)
        all_sprites_surf.add(wall9)
        wall_sprites.add(wall1)
        wall_sprites.add(wall2)
        wall_sprites.add(wall3)
        wall_sprites.add(wall4)
        wall_sprites.add(wall5)
        wall_sprites.add(wall6)
        wall_sprites.add(wall7)
        wall_sprites.add(wall8)
        wall_sprites.add(wall9)

        player.update_position()
        enemy5.update_position()
        enemy7.update_position()

        # Calculates time
        time = (pygame.time.get_ticks() - start_ticks) / 1000 #calculate how many seconds
        # Change view cone
        if time > 2:
            start_ticks = pygame.time.get_ticks()
        
        # Enemy 1
            if cone1_state > 1:
                cone1_state = 0
            if cone1_state == 0:
                cone1.kill()
                cone1 = Cone([300, 510], orientation="r")
                cone_sprites.add(cone1)
            elif cone1_state == 1:
                cone1.kill()
                cone1 = Cone([300, 510], orientation="d")
                cone_sprites.add(cone1)
            cone1_state += 1

        # Enemy 2
            if cone2_state > 1:
                cone2_state = 0
            if cone2_state == 0:
                cone2.kill()
                cone2 = Cone([850, 650], orientation="r")
                cone_sprites.add(cone2)
            elif cone2_state == 1:
                cone2.kill()
                cone2 = Cone([850, 650], orientation="u")
                cone_sprites.add(cone2)
            cone2_state += 1

        # Enemy 3
            if cone3_state > 3:
                cone3_state = 0
            if cone3_state == 0:
                cone3.kill()
                cone3 = Cone([1100, 350], orientation="l")
                cone_sprites.add(cone3)
            elif cone3_state == 1:
                cone3.kill()
                cone3 = Cone([1100, 350], orientation="d")
                cone_sprites.add(cone3)
            elif cone3_state == 2:
                cone3.kill()
                cone3 = Cone([1100, 350], orientation="r")
                cone_sprites.add(cone3)
            elif cone3_state == 3:
                cone3.kill()
                cone3 = Cone([1100, 350], orientation="u")
                cone_sprites.add(cone3)
            cone3_state += 1

        # Enemy 4
            if cone4_state > 3:
                cone4_state = 0
            if cone4_state == 0:
                cone4.kill()
                cone4 = Cone([730, 350], orientation="l")
                cone_sprites.add(cone4)
            elif cone4_state == 1:
                cone4.kill()
                cone4 = Cone([730, 350], orientation="d")
                cone_sprites.add(cone4)
            elif cone4_state == 2:
                cone4.kill()
                cone4 = Cone([730, 350], orientation="r")
                cone_sprites.add(cone4)
            elif cone4_state == 3:
                cone4.kill()
                cone4 = Cone([730, 350], orientation="u")
                cone_sprites.add(cone4)
            cone4_state += 1

        # Enemy 6
            if cone6_state > 3:
                cone6_state = 0
            if cone6_state == 0:
                cone6.kill()
                cone6 = Cone([605, 100], orientation="u")
                cone_sprites.add(cone6)
            elif cone6_state == 1:
                cone6.kill()
                cone6 = Cone([605, 100], orientation="r")
                cone_sprites.add(cone6)
            elif cone6_state == 2:
                cone6.kill()
                cone6 = Cone([605, 100], orientation="d")
                cone_sprites.add(cone6)
            elif cone6_state == 3:
                cone6.kill()
                cone6 = Cone([605, 100], orientation="l")
                cone_sprites.add(cone6)
            cone6_state += 1

        # Print all sprites
        for entity in all_sprites_surf:
            screen.blit(entity.surf, entity.rect)
        for entity in all_sprites_img:
            screen.blit(entity.image, entity.rect)

        # Enemy collision
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False

        # Flag collision
        if pygame.sprite.collide_rect(player, endflag):
            running = False
            end = True

        # Vision cone collision
        for cone in cone_sprites:
            for rect in cone.rect:
                if player.rect.colliderect(rect):
                    player.kill()
                    running = False
        for entity in cone_sprites:
            screen.blit(entity.image, entity.rect[0])
            for rect in entity.rect:
                screen.blit(entity.surf, rect)

        # Wall collision
        if pygame.sprite.spritecollideany(player, wall_sprites):
            col_wall = pygame.sprite.spritecollide(player, wall_sprites, False)[0]
            if player.rect.left < col_wall.rect.right < player.rect.right:
                player.rect.left = col_wall.rect.right
            elif player.rect.top < col_wall.rect.bottom < player.rect.bottom:
                player.rect.top = col_wall.rect.bottom
            elif player.rect.bottom > col_wall.rect.top > player.rect.top:
                player.rect.bottom = col_wall.rect.top
            elif player.rect.right > col_wall.rect.left > player.rect.left:
                player.rect.right = col_wall.rect.left

        # Keep at bottom for display reasons
        pygame.display.flip()
        
        # Initialize frame rate
        clock.tick(30)
        pass

    pygame.quit()

if __name__ == "__main__":
    run()