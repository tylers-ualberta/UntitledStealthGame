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
            self.surfFlag = True
        else:
            self.rect = pygame.Rect(offset[0], offset[1], 15, 40)
            self.image = pygame.image.load(sprite)
            self.surfFlag = False
            self.AnimationCount = 0
        return

    def update_position(self):
        if self.surfFlag:
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
        else:
            keys = pygame.key.get_pressed()  # Get pressed idea: https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down
            if keys[K_w]:
                self.rect.move_ip(0, -4)
                if self.AnimationCount <= 5:
                    self.image = pygame.image.load('Assets/PlayerWalking.png')
                    self.AnimationCount += 1
                elif self.AnimationCount <= 10:
                    self.image = pygame.image.load('Assets/Player.png')
                    self.AnimationCount += 1
                else:
                    self.AnimationCount = 0
            if keys[K_a]:
                self.rect.move_ip(-4, 0)
                if self.AnimationCount <= 5:
                    self.image = pygame.image.load('Assets/PlayerWalking.png')
                    self.AnimationCount += 1
                elif self.AnimationCount <= 10:
                    self.image = pygame.image.load('Assets/Player.png')
                    self.AnimationCount += 1
                else:
                    self.AnimationCount = 0
            if keys[K_s]:
                self.rect.move_ip(0, 4)
                if self.AnimationCount <= 5:
                    self.image = pygame.image.load('Assets/PlayerWalking.png')
                    self.AnimationCount += 1
                elif self.AnimationCount <= 10:
                    self.image = pygame.image.load('Assets/Player.png')
                    self.AnimationCount += 1
                else:
                    self.AnimationCount = 0
            if keys[K_d]:
                self.rect.move_ip(4, 0)
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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, offset, colour=(255, 255, 0), sprite=""):
        super(Enemy, self).__init__()
        if sprite == "":
            self.surf = pygame.Surface((0,0))
            self.surf.fill(colour)
            self.rect = self.surf.get_rect()
            self.rect.move_ip(offset)
        else:
            self.rect = pygame.Rect(offset[0], offset[1], 20, 40)
            self.image = pygame.image.load(sprite)
        self.offset = offset

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        return


class MovingEnemy(Enemy):
    """ MovingEnemy is used to create a moving enemy. Please follow the arguements
    as written to properly create the moving enemy.

    Arguements: (all measurements taken from top left corner, which is [0,0])
    offset; the starting position of the enemy, enter as a list of integers.

    rang; the points that the enemy is to move to. Enter as a list of tuples.
    The last tuple entered is the position you want the enemy to end up at.
    Always keep one of (x, y) constant across two points, when the enemy reaches
    the last point it will loop back to the first point.

    speed; set the speed of the enemy, enter as an int.
    """
    def __init__(self, offset, rang, speed=0, colour=(0, 255, 0), sprite=""):
        super().__init__(offset, colour, sprite)
        self.range = rang
        self.pos = offset
        self.target = [rang[0][0], rang[0][1]]
        self.index = 0
        self.speed = speed
        self.maxIndex = len(rang) - 1
        self.carrySpeed = 0
        return

    def update_position(self):
        diffX = self.pos[0] - self.target[0]
        diffY = self.pos[1] - self.target[1]
        if max(abs(diffX), abs(diffY)) < self.speed:
            if diffX != 0:
                if diffX < 0:
                    remSpeed = self.speed + diffX
                    print(remSpeed)
                    self.carrySpeed = self.speed - remSpeed
                    self.rect.move_ip(remSpeed, 0)
                    self.pos[0] = self.pos[0] + remSpeed
                else:
                    remSpeed = self.speed - diffX
                    self.carrySpeed = self.speed - remSpeed
                    self.rect.move_ip(-remSpeed, 0)
                    self.pos[0] = self.pos[0] - remSpeed
            else:
                if diffY < 0:
                    remSpeed = self.speed + diffY
                    self.carrySpeed = self.speed - remSpeed
                    self.rect.move_ip(0, remSpeed)
                    self.pos[1] = self.pos[1] + remSpeed
                else:
                    remSpeed = self.speed - diffY
                    self.carrySpeed = self.speed - remSpeed
                    self.rect.move_ip(0, -remSpeed)
                    self.pos[1] = self.pos[1] - remSpeed

        else:
            if diffX != 0:
                if diffX < 0:
                    self.rect.move_ip(self.speed + self.carrySpeed, 0)
                    self.pos[0] = self.pos[0] + self.speed + self.carrySpeed
                else:
                    self.rect.move_ip(-self.speed - self.carrySpeed, 0)
                    self.pos[0] = self.pos[0] - self.speed - self.carrySpeed
                self.carrySpeed = 0
            else:
                if diffY < 0:
                    self.rect.move_ip(0, self.speed + self.carrySpeed)
                    self.pos[1] = self.pos[1] + self.speed + self.carrySpeed
                else:
                    self.rect.move_ip(0, -self.speed - self.carrySpeed)
                    self.pos[1] = self.pos[1] - self.speed - self.carrySpeed
                self.carrySpeed = 0
        if self.pos == self.target:
            self.index += 1
            if self.index > self.maxIndex:
                self.index = 0
            self.target = [self.range[self.index][0], self.range[self.index][1]]
        return


class Item(pygame.sprite.Sprite):
    def __init__(self, offset, colour=(255, 0, 0), sprite=""):
        super(Item, self).__init__()
        if sprite == "":
            self.surf = pygame.Surface((5, 5))
            self.surf.fill(colour)
            self.rect = self.surf.get_rect()
            self.rect.move_ip(offset)
        else:
            self.rect = pygame.Rect(offset[0], offset[1], 25, 40)
            self.image = pygame.image.load(sprite)
        return
    
    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        return


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
    def __init__(self, offset, orientation="l", colour=(255, 255, 0)):
        super().__init__(offset, colour=(255, 0, 0))
        self.image = pygame.image.load(r"Hackathon/Assets/Cone.png")
        self.orient(offset, orientation)
        self.image = pygame.transform.scale2x(self.image)
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        # Change self.rect to be hitbox DELETE
        if orientation=="l":
            self.rect = [pygame.Rect(offset[0], offset[1], 0, 0), pygame.Rect(offset[0], offset[1] + 9, 32, 80),
                        pygame.Rect(offset[0] + 32, offset[1] + 18, 32, 60), pygame.Rect(offset[0] + 64, offset[1] + 27, 32, 40), 
                        pygame.Rect(offset[0] + 96, offset[1] + 36, 32, 20), pygame.Rect(offset[0] + 112, offset[1] + 42, 16, 10)]
        elif orientation=="r":
            print(self.offset)
            self.rect = [pygame.Rect(offset[0], offset[1], 0, 0), pygame.Rect(offset[0] + 138, offset[1], 32, 80),
                        pygame.Rect(offset[0] + 122, offset[1] + 18, 32, 60), pygame.Rect(offset[0] + 90, offset[1] + 27, 32, 40), 
                        pygame.Rect(offset[0] + 58, offset[1] + 36, 32, 20), pygame.Rect(offset[0] + 24, offset[1] + 42, 16, 10)]
        elif orientation=="u":
            self.rect = [pygame.Rect(offset[0], offset[1], 0, 0), pygame.Rect(offset[0] + 10, offset[1], 80, 32),
                        pygame.Rect(offset[0] + 19, offset[1] + 32, 60, 32), pygame.Rect(offset[0] + 27, offset[1] + 64, 40, 32), 
                        pygame.Rect(offset[0] + 36, offset[1] + 96, 20, 32), pygame.Rect(offset[0] + 44, offset[1] + 112, 10, 16)]
        else:
            self.rect = [pygame.Rect(offset[0], offset[1], 0, 0), pygame.Rect(offset[0] + 8, offset[1] + 138, 80, 32),
                        pygame.Rect(offset[0] + 17, offset[1] + 122, 60, 32), pygame.Rect(offset[0] + 25, offset[1] + 90, 40, 32), 
                        pygame.Rect(offset[0] + 34, offset[1] + 58, 20, 32), pygame.Rect(offset[0] + 42, offset[1] + 26, 10, 16)]
        self.offset = offset

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        return

    def orient(self, offset, orientation):
        # Adjust offset to be centered on enemy
        if orientation == "l":
            self.offset[0] -= 160
            self.offset[1] -= 40
        elif orientation == "r":
            self.offset[0] += 23
            self.offset[1] -= 40
            self.image = pygame.transform.rotate(self.image, 180)
        elif orientation == "d":
            self.offset[0] -= 38
            self.offset[1] += 40
            self.image = pygame.transform.rotate(self.image, 90)
        elif orientation == "u":
            self.offset[0] -= 38
            self.offset[1] -= 160
            self.image = pygame.transform.rotate(self.image, 270)
        return


def main():
    width, height = 1260, 700
    screen = pygame.display.set_mode([width, height], HWSURFACE|DOUBLEBUF)
    player = Player([1210, 650])
    flagL = Cone([200, 200])
    flagR = Cone([200, 200], 'r')
    flagU = Cone([500, 500], 'u')
    flagD = Cone([700, 450], 'd')

    all_sprites_surf = pygame.sprite.Group()
    all_sprites_img = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    items = pygame.sprite.Group()
    cone_sprites = pygame.sprite.Group()
    cone_sprites.add(flagL)
    cone_sprites.add(flagR)
    cone_sprites.add(flagD)
    cone_sprites.add(flagU)
    all_sprites_surf.add(player)
    # INCLUDE IN YOUR LEVEL:
    screen = pygame.display.set_mode([1260, 700], HWSURFACE|DOUBLEBUF)
    running = True
    # Add all sprites to their appropriate sprite group(s). Any sprites from the
    # assests folder need to be in all_sprites_img.
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

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False


        # if pygame.sprite.collide_rect(player, Item):
        #     running = False
        
        # Vision cone collision
        for cone in cone_sprites:
            for rect in cone.rect:
                if player.rect.colliderect(rect):
                    player.kill()
                    running = False

        # Wall collision
        if pygame.sprite.spritecollideany(player, wall_sprites):
            col_wall = pygame.sprite.spritecollide(player, wall_sprites, False)[0]
            if player.rect.top < col_wall.rect.bottom < player.rect.bottom:
                player.rect.top = col_wall.rect.bottom
            elif player.rect.left < col_wall.rect.right < player.rect.right:
                player.rect.left = col_wall.rect.right
            elif player.rect.bottom > col_wall.rect.top > player.rect.top:
                player.rect.bottom = col_wall.rect.top
            elif player.rect.right > col_wall.rect.left > player.rect.left:
                player.rect.right = col_wall.rect.left
if __name__ == "__main__":
    # main() used for testing new class functions
    main()