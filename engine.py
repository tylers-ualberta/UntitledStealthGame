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
            print(self.rect)
        else:
            self.rect = pygame.Rect(offset[0], offset[1], 15, 40)
            self.image = pygame.image.load(sprite)
            self.AnimationCount = 0

    def update_position(self):
        keys = pygame.key.get_pressed()  # Get pressed idea: https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down
        if keys[K_w]:
            self.rect.move_ip(0, -2)
            if self.AnimationCount <= 5:
                self.image = pygame.image.load('Assets/PlayerWalking.png')
                self.AnimationCount += 1
            elif self.AnimationCount <= 10:
                self.image = pygame.image.load('Assets/Player.png')
                self.AnimationCount += 1
            else:
                self.AnimationCount = 0
        if keys[K_a]:
            self.rect.move_ip(-2, 0)
            if self.AnimationCount <= 5:
                self.image = pygame.image.load('Assets/PlayerWalking.png')
                self.AnimationCount += 1
            elif self.AnimationCount <= 10:
                self.image = pygame.image.load('Assets/Player.png')
                self.AnimationCount += 1
            else:
                self.AnimationCount = 0
        if keys[K_s]:
            self.rect.move_ip(0, 2)
            if self.AnimationCount <= 5:
                self.image = pygame.image.load('Assets/PlayerWalking.png')
                self.AnimationCount += 1
            elif self.AnimationCount <= 10:
                self.image = pygame.image.load('Assets/Player.png')
                self.AnimationCount += 1
            else:
                self.AnimationCount = 0
        if keys[K_d]:
            self.rect.move_ip(2, 0)
            if self.AnimationCount <= 5:
                self.image = pygame.image.load('Assets/PlayerWalking.png')
                self.AnimationCount += 1
            elif self.AnimationCount <= 10:
                self.image = pygame.image.load('Assets/Player.png')
                self.AnimationCount += 1
            else:
                self.AnimationCount = 0
        return
    
    def draw(self, screen):
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
        self.offset = offset


    def resize(self, dWidth, dHeight):
        self.rect.move_ip(-dWidth, -dHeight)
        return

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        return

class Camera(Enemy):
    def __init__(self, offset, sweep, colour=(255, 255, 0), sprite=""):
        super().__init__(self, offset, 0, colour, sprite)
        self.sweep = sweep
        return


class StationaryEnemy(Enemy):
    def __init__(self, offset, sweep, colour=(255, 255, 0), sprite=""):
        super().__init__(self, offset, 0, colour, sprite)
        self.sweep = sweep
        return


class MovingEnemy(Enemy):
    def __init__(self, offset, rang, speed=0, colour=(255, 255, 0), sprite=""):
        super().__init__(self, offset, speed, colour, sprite)
        self.range = rang
        self.pos = offset
        return

    def update_position():
        self.pos


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
    
    def draw(self, screen):
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
    
    def draw(self, screen):
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
        if orientation == "l":
            offset[0] -= 160
            offset[1] -= 40
        elif orientation == "r":
            offset[0] += 23
            offset[1] -= 40
            self.image = pygame.transform.rotate(self.image, 180)
        elif orientation == "d":
            offset[0] -= 38
            offset[1] += 40
            self.image = pygame.transform.rotate(self.image, 90)
        elif orientation == "u":
            offset[0] -= 38
            offset[1] -= 160
            self.image = pygame.transform.rotate(self.image, 270)

def main():
    width, height = 1260, 700
    screen = pygame.display.set_mode([width, height], RESIZABLE|HWSURFACE|DOUBLEBUF)
    player = Player([1210, 650])
    all_sprites = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    items = pygame.sprite.Group()
    all_sprites.add(player)
    # INCLUDE IN YOUR LEVEL:
    key = Item([400, 400])
    wallB1 = Walls([0, 0], screen.get_width(), 10)
    wallB2 = Walls([0, 0], 10, screen.get_height())
    wallB3 = Walls([0, screen.get_height()-10], screen.get_width(), 10)
    wallB4 = Walls([screen.get_width()-10, 0], 10, screen.get_height())
    all_sprites.add(key)
    all_sprites.add(wallB1)
    all_sprites.add(wallB2)
    all_sprites.add(wallB3)
    all_sprites.add(wallB4)
    wall_sprites.add(wallB1)
    wall_sprites.add(wallB2)
    wall_sprites.add(wallB3)
    wall_sprites.add(wallB4)
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
                for wall in wall_sprites:
                    wall.kill()
                wallB1 = Walls([0, 0], screen.get_width(), 10)
                wallB2 = Walls([0, 0], 10, screen.get_height())
                wallB3 = Walls([0, screen.get_height()-10], screen.get_width(), 10)
                wallB4 = Walls([screen.get_width()-10, 0], 10, screen.get_height())
                wall_sprites.add(wallB1)
                wall_sprites.add(wallB2)
                wall_sprites.add(wallB3)
                wall_sprites.add(wallB4)
                all_sprites.add(wallB1)
                all_sprites.add(wallB2)
                all_sprites.add(wallB3)
                all_sprites.add(wallB4)
                width, height = event.w, event.h
                
        # Sets screen colour
        screen.fill((255, 255, 255))
        # Draws boarder walls
        player.update_position()
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
        # Sets our framerate
        clock.tick(60)
    pygame.quit()
    return

if __name__ == "__main__":
    # main() used for testing new class functions
    main()