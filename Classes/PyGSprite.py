import pygame
import os

from Classes.Direction import Direction

IMG_PATH="img"

class PyGSprite(pygame.sprite.Sprite):
    SPRITE_SIZE = 100
    def __init__(self, sprite_name, posX, posY, playground):
        pygame.sprite.Sprite.__init__(self)
        self.playground = playground
        self.image = pygame.image.load(os.path.join(IMG_PATH, sprite_name)).convert_alpha()
        self.rect = self.image.get_rect().move(posX, posY)
        self.direction = Direction.RIGHT
        self.old_pos = self.rect;

    def rotate(self,old, new):
        if old == Direction.RIGHT:
            if new == Direction.LEFT:
                self.image = pygame.transform.rotate(self.image, 180.0)
            elif new == Direction.UP:
                self.image = pygame.transform.rotate(self.image, 90.0)
            elif new == Direction.DOWN:
                self.image = pygame.transform.rotate(self.image, -90.0)
        elif old == Direction.UP:
            if new == Direction.LEFT:
                self.image = pygame.transform.rotate(self.image, 90.0)
            elif new == Direction.RIGHT:
                self.image = pygame.transform.rotate(self.image, -90.0)
            elif new == Direction.DOWN:
                self.image = pygame.transform.rotate(self.image, 180.0)
        elif old == Direction.LEFT:
            if new == Direction.RIGHT:
                self.image = pygame.transform.rotate(self.image, 180.0)
            elif  new == Direction.UP:
                self.image = pygame.transform.rotate(self.image, -90.0)
            elif   new == Direction.DOWN:
                self.image = pygame.transform.rotate(self.image, 90.0)
        elif old == Direction.DOWN:
            if new == Direction.LEFT:
                self.image = pygame.transform.rotate(self.image, -90.0)
            elif  new == Direction.UP:
                self.image = pygame.transform.rotate(self.image, 180.0)
            elif new == Direction.RIGHT:
                self.image = pygame.transform.rotate(self.image, 90.0)

    def fallBack(self):
        self.rect = self.old_pos
        
    def move(self, x, y):
        self.old_pos = self.rect
        self.playground.screen.blit(self.playground.background, self.rect, self.rect)
        self.rect = self.rect.move(x, y)
        pygame.time.wait(500)

    def up(self):
        print("Player up")
        self.rotate(self.direction, Direction.UP)
        self.move(0, -50)
        self.direction = Direction.UP

    def down(self):
        print("Player down")
        self.rotate(self.direction, Direction.DOWN)
        self.move(0, 50)
        self.direction = Direction.DOWN

    def right(self):
        print("Player right")
        self.rotate(self.direction, Direction.RIGHT)
        self.move(50, 0)
        self.direction = Direction.RIGHT

    def left(self):
        print("Player left")
        self.rotate(self.direction, Direction.LEFT)
        self.move(-50, 0)
        self.direction = Direction.LEFT
