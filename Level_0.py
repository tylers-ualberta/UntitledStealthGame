import pygame
from engine import *
from pygame.locals import *

""" Provide the necessary info for the main game to be able to generate the
level.

Level: 0

Description: Tutorial level

"""

pygame.init()

# Main function that runs
def run():
    end = False
    screen = pygame.display.set_mode([1260, 700], HWSURFACE|DOUBLEBUF)
    running = True

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
    wall1 = Walls([0, 10], screen.get_width(), 100)
    wall2 = Walls([screen.get_width() - 115, 0], 115, screen.get_height())
    wall3 = Walls([0, screen.get_height()-100], screen.get_width(), 100)
    wall4 = Walls([0, screen.get_height()/2-100], 3*screen.get_width()/4+10, 200)
    all_sprites_surf.add(wall1)
    all_sprites_surf.add(wall2)
    all_sprites_surf.add(wall3)
    all_sprites_surf.add(wall4)
    wall_sprites.add(wall1)
    wall_sprites.add(wall2)
    wall_sprites.add(wall3)
    wall_sprites.add(wall4)

    # Entity spawn conditions
    # offset indicates player spawn point
    offset = [200, screen.get_height()-150]
    # Set enemy spawn
    e_spawn1 = [3*screen.get_width()/4+20, screen.get_height()/2-10]
    # Set goal location
    goal = [50, screen.get_height()/5+20]

    # Initializing players and enemies
    player = Player(offset, sprite="Assets/Player.png")
    enemy = Enemy(e_spawn1, sprite="Assets/SecurityGuard.png")
    cone = Cone(e_spawn1, orientation="r")
    endflag = Item(goal, sprite="Assets/EndFlag.png")
    all_sprites_img.add(player)
    all_sprites_img.add(enemy)
    enemies.add(enemy)
    cone_sprites.add(cone)
    all_sprites_img.add(endflag)
    items.add(endflag)

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
        screen.fill((255, 255, 255))
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
                cone_sprites.add(cone)
            elif cone_state == 1:
                cone.kill()
                cone = Cone([3*screen.get_width()/4+20, screen.get_height()/2-10], orientation="r")
                cone_sprites.add(cone)
            elif cone_state == 2:
                cone.kill()
                cone = Cone([3*screen.get_width()/4+20, screen.get_height()/2-10], orientation="u")
                cone_sprites.add(cone)
            elif cone_state == 3:
                cone.kill()
                cone = Cone([3*screen.get_width()/4+20, screen.get_height()/2-10], orientation="r")
                cone_sprites.add(cone)
            cone_state += 1

        # Drawing
        for entity in all_sprites_img:
            screen.blit(entity.image, entity.rect)

        # Walls
        for entity in all_sprites_surf:
            screen.blit(entity.surf, entity.rect)
        
        for entity in cone_sprites:
            screen.blit(entity.image, entity.rect[0])
            for rect in entity.rect:
                screen.blit(entity.surf, rect)
        pygame.display.flip()

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

        # Wall collision
        if pygame.sprite.spritecollideany(player, wall_sprites):
            col_walls = (pygame.sprite.spritecollide(player, wall_sprites, False))
            if len(col_walls) == 2:
                col_wall = col_walls[0]
                if player.rect.left < col_wall.rect.right < player.rect.right:
                    player.rect.move_ip(5, 0)
                elif player.rect.top < col_wall.rect.bottom < player.rect.bottom:
                    player.rect.move_ip(0, 5)
                elif player.rect.bottom > col_wall.rect.top > player.rect.top:
                    player.rect.move_ip(0, -5)
                elif player.rect.right > col_wall.rect.left > player.rect.left:
                    player.rect.move_ip(-5, 0)
                col_wall2 = col_walls[1]
                if player.rect.left < col_wall2.rect.right < player.rect.right:
                    player.rect.move_ip(5, 0)
                elif player.rect.top < col_wall2.rect.bottom < player.rect.bottom:
                    player.rect.move_ip(0, 5)
                elif player.rect.bottom > col_wall2.rect.top > player.rect.top:
                    player.rect.move_ip(0, -5)
                elif player.rect.right > col_wall2.rect.left > player.rect.left:
                    player.rect.move_ip(-5, 0)
            else:
                col_wall = pygame.sprite.spritecollide(player, wall_sprites, False)[0]
                if player.rect.left < col_wall.rect.right < player.rect.right:
                    player.rect.move_ip(5, 0)
                elif player.rect.top < col_wall.rect.bottom < player.rect.bottom:
                    player.rect.move_ip(0, 5)
                elif player.rect.bottom > col_wall.rect.top > player.rect.top:
                    player.rect.move_ip(0, -5)
                elif player.rect.right > col_wall.rect.left > player.rect.left:
                    player.rect.move_ip(-5, 0)

        # Keep at bottom for display reasons
        pygame.display.flip()
        
        # Initialize frame rate
        clock.tick(30)
    return end


if __name__ == "__main__":
    run()
    pygame.quit()
