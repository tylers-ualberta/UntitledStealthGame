# INCLUDE IN YOUR LEVEL:
screen = pygame.display.set_mode([1260, 700], HWSURFACE|DOUBLEBUF)
running = True
# Add all sprites to their appropriate sprite group(s). Any sprites from the
# assests folder need to be in all_sprites_img.
all_sprites_surf = pygame.sprite.Group()
all_sprites_img = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()
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
while running:
    # Handles quitting the game, resizing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            
    # Sets screen colour
    screen.fill((255, 255, 255))
    # Updates player's position each loop
    for entity in all_sprites_surf:
        screen.blit(entity.surf, entity.rect)
    for entity in all_sprites_img:
        screen.blit(entity.image, entity.rect)
    pygame.display.flip()
    # Sets our framerate
    clock.tick(60)
pygame.quit()