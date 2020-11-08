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
    if pygame.sprite.collide_rect(player, Item):
        running = False

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
                player.rect.left = col_wall.rect.right
            elif player.rect.top < col_wall.rect.bottom < player.rect.bottom:
                player.rect.top = col_wall.rect.bottom
            elif player.rect.bottom > col_wall.rect.top > player.rect.top:
                player.rect.bottom = col_wall.rect.top
            elif player.rect.right > col_wall.rect.left > player.rect.left:
                player.rect.right = col_wall.rect.left
            col_wall2 = col_walls[1]
            if player.rect.left < col_wall2.rect.right < player.rect.right:
                player.rect.left = col_wall2.rect.right
            elif player.rect.top < col_wall2.rect.bottom < player.rect.bottom:
                player.rect.top = col_wall2.rect.bottom
            elif player.rect.bottom > col_wall2.rect.top > player.rect.top:
                player.rect.bottom = col_wall2.rect.top
            elif player.rect.right > col_wall2.rect.left > player.rect.left:
                player.rect.right = col_wall2.rect.left
        else:
            col_wall = pygame.sprite.spritecollide(player, wall_sprites, False)[0]
            if player.rect.left < col_wall.rect.right < player.rect.right:
                player.rect.left = col_wall.rect.right
            elif player.rect.top < col_wall.rect.bottom < player.rect.bottom:
                player.rect.top = col_wall.rect.bottom
            elif player.rect.bottom > col_wall.rect.top > player.rect.top:
                player.rect.bottom = col_wall.rect.top
            elif player.rect.right > col_wall.rect.left > player.rect.left:
                player.rect.right = col_wall.rect.left
    # Sets our framerate
    clock.tick(60)
pygame.quit()