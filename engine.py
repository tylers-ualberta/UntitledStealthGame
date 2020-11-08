import pygame
from pygame.locals import *
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, offset, sprite=""):
        super(Player, self).__init__()
        if sprite == "":
            self.surf = pygame.Surface((20, 20))
            self.surf.fill((0, 0, 255))
            self.rect = self.surf.get_rect()
            self.rect.move_ip(offset)
        else:
            self.rect = pygame.Rect(offset[0], offset[1], 20, 40)
            self.image = pygame.image.load(sprite)

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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, offset, speed=0, colour=(255, 255, 0), sprite=""):
        super(Enemy, self).__init__()
        if sprite == "":
            self.surf = pygame.Surface((20,20))
            self.surf.fill(colour)
            self.rect = self.surf.get_rect()
            self.rect.move_ip(offset)
        else:
            self.rect = pygame.Rect(offset[0], offset[1], 20, 40)
            self.image = pygame.image.load(sprite)

        self.speed = speed

    def resize(self, dWidth, dHeight):
        self.rect.move_ip(-dWidth, -dHeight)
        return

    def draw(self):
        screen.blit(self.surf, self.rect)
        pass


class Item(pygame.sprite.Sprite):
    def __init__(self, offset, colour=(255, 0, 0), sprite=""):
        super(Item, self).__init__()
        self.surf = pygame.Surface((5, 5))
        self.surf.fill(colour)
        self.rect = self.surf.get_rect()
        self.offset = offset
        self.rect.move_ip(offset)
        pass
    
    def resize(self, dWidth, dHeight):
        self.rect.move_ip(-dWidth, -dHeight)
        return
    
    def draw(self):
        screen.blit(self.surf, self.rect)
        pass


class Walls(pygame.sprite.Sprite):
    def __init__(self, corner, width, height, colour=(0,0,0)):
        super(Walls, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(colour)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(corner)
        return
    
    def draw(self):
        screen.blit(self.surf, self.rect)
        return

class Cone(Enemy):
    def __init__(self, offset, orientation="left", speed=0, colour=(255, 255, 0)):
        super().__init__(offset, speed=0, colour=(255, 255, 0))
        self.image = pygame.image.load("Assets/Cone.png").convert()
        self.orient(offset, orientation)
        self.image = pygame.transform.scale2x(self.image)
        self.image.set_colorkey((255, 255, 255), RLEACCEL)


        # Change self.rect to be hitbox DELETE
        self.rect = self.surf.get_rect()
        self.offset = offset
        self.speed = speed
        self.rect.move_ip(offset)

    def resize(self, dWidth, dHeight):
        self.rect.move_ip(-dWidth, -dHeight)
        return

    def draw(self):
        screen.blit(self.surf, self.rect)
        pass

    def orient(self, offset, orientation):
        # Adjust offset to be centered on enemy
        if orientation == "left":
            offset[0] -= 160
            offset[1] -= 40
        elif orientation == "right":
            offset[0] += 20 # Actual width of enemy
            offset[1] -= 40 # Twice the size
            self.image = pygame.transform.rotate(self.image, 180)

def main():
    width, height = 1260, 700
    screen = pygame.display.set_mode([width, height], RESIZABLE|HWSURFACE|DOUBLEBUF)
    player = Player([1210, 650])
    # INCLUDE IN YOUR LEVEL:
    key = Item([400, 400])
    wallB1 = Walls([0, 0], screen.get_width(), 10)
    wallB2 = Walls([0, 0], 10, screen.get_height())
    wallB3 = Walls([0, screen.get_height()-10], screen.get_width(), 10)
    wallB4 = Walls([screen.get_width()-10, 0], 10, screen.get_height())
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
                wallB1 = Walls([0, 0], screen.get_width(), 10)
                wallB2 = Walls([0, 0], 10, screen.get_height())
                wallB3 = Walls([0, screen.get_height()-10], screen.get_width(), 10)
                wallB4 = Walls([screen.get_width()-10, 0], 10, screen.get_height())
                width, height = event.w, event.h
                
        # Sets screen colour
        screen.fill((255, 255, 255))
        # Draws boarder walls
        wallB1.draw()
        wallB2.draw()
        wallB3.draw()
        wallB4.draw()
        key.draw()
        # Updates player's position each loop
        player.update_position()
        player.draw()
        pygame.display.flip()
        # Sets our framerate
        clock.tick(60)
    pygame.quit()
    return
if __name__ == "__main__":
    screen = pygame.display.set_mode([1260, 700], RESIZABLE|HWSURFACE|DOUBLEBUF)
    # main() used for testing new class functions
    main()