import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([1260, 700], RESIZABLE|HWSURFACE|DOUBLEBUF)

class Characters():
    def get_location(self):
        return(self.location)
    
    def resize(self):
        self.location = (screen.get_width()-self.offset[0], screen.get_height()-self.offset[1])
        return


class Player(pygame.sprite.Sprite):
    def __init__(self, offset):
        super(Player, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(offset)

    def update_position(self):
        keys = pygame.key.get_pressed()  # Get pressed idea: https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down
        if keys[K_w]:
            self.rect.move_ip(0, -2)
        if keys[K_a]:
            self.rect.move_ip(-2, 0)
        if keys[K_s]:
            self.rect.move_ip(0, 2)
        if keys[K_d]:
            self.rect.move_ip(2, 0)
        return
    
    def draw(self):
        screen.blit(self.surf, self.rect)
        return
    
    def resize(self, dWidth, dHeight):
        self.rect.move_ip(-dWidth, -dHeight)
        return


class Enemy(Characters):
    def __init__(self, offset):
        self.offset = offset
        self.location = (screen.get_width()-self.offset[0], screen.get_height()-self.offset[0])


class Item(Characters):
    def __init__(self, offset):
        pass


class Walls():
    def __init__(self, corner):
        pass


def main():
    player = Player([1210, 650])
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
    return
if __name__ == "__main__":
    # main() used for testing new class functions
    main()