import pygame
from pygame.locals import *
from engine import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, offset, colour=(255, 255, 0), sprite=""):
        super(Enemy, self).__init__()
        self.rect = pygame.Rect(offset[0], offset[1], 20, 40)
        self.image = pygame.image.load(sprite)

    def double(self):
        pygame.transform.scale2x(self.image)

def dying():
    running = True
    screen = pygame.display.set_mode([1260, 700], HWSURFACE|DOUBLEBUF)
    screen.fill((255, 255, 255))
    enemy1 = Enemy([530, 350], sprite="Assets/SecurityGuard.png")

    clock = pygame.time.Clock()
    while running:
        start_ticks = pygame.time.get_ticks()
        time = (pygame.time.get_ticks() - start_ticks) / 1000





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if time > 0.66:
            start_ticks = pygame.time.get_ticks()
            enemy1.double()


        screen.blit(enemy1.image, enemy1.rect)







        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    dying()
