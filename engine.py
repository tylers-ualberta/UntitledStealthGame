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


class Player(Characters):
    def __init__(self, offset):
        self.offset = offset
        self.location = (screen.get_width()-self.offset[0], screen.get_height()-self.offset[0])
        return
    
    def update_position(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.offset[1] += 2
            self.location = (screen.get_width()-self.offset[0], screen.get_height()-self.offset[1])
        if keys[K_a]:
            self.offset[0] += 2
            self.location = (screen.get_width()-self.offset[0], screen.get_height()-self.offset[1])
        if keys[K_s]:
            self.offset[1] -= 2
            self.location = (screen.get_width()-self.offset[0], screen.get_height()-self.offset[1])
        if keys[K_d]:
            self.offset[0] -= 2
            self.location = (screen.get_width()-self.offset[0], screen.get_height()-self.offset[1])
        return

    def draw(self):
        pygame.draw.circle(screen, (0, 0, 255), self.location, 10)
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
    player = Player([50, 50])

    # INCLUDE IN YOUR LEVEL:
    screen = pygame.display.set_mode([1260, 700], RESIZABLE|HWSURFACE|DOUBLEBUF)
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
                player.resize()
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


        #BELOW HERE IS CODE USED FOR TESTING PURPOSES ONLY
        

    pygame.quit()
    return
if __name__ == "__main__":
    # main() used for testing new class functions
    main()