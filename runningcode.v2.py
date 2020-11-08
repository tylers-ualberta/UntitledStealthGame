# INCLUDE IN YOUR LEVEL:
width, height = 1260, 700
screen = pygame.display.set_mode([width, height], RESIZABLE|HWSURFACE|DOUBLEBUF)
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
            # Keeps the player's position constant
            dw, dh = width - event.w, height - event.h
            player.resize(dw, dh)
            width, height = event.w, event.h
            
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
pygame.quit()