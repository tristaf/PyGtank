import pygame
import os
import queue

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
        self.new_pos = (posX, posY)
        self.moved = False
        self.cmdFIFO = queue.Queue()

    def rotate(self, direction):
        if self.direction == Direction.RIGHT:
            if direction == Direction.LEFT:
                self.image = pygame.transform.rotate(self.image, 180.0)
            elif direction == Direction.UP:
                self.image = pygame.transform.rotate(self.image, 90.0)
            elif direction == Direction.DOWN:
                self.image = pygame.transform.rotate(self.image, -90.0)
        elif self.direction == Direction.UP:
            if direction == Direction.LEFT:
                self.image = pygame.transform.rotate(self.image, 90.0)
            elif direction == Direction.RIGHT:
                self.image = pygame.transform.rotate(self.image, -90.0)
            elif direction == Direction.DOWN:
                self.image = pygame.transform.rotate(self.image, 180.0)
        elif self.direction == Direction.LEFT:
            if direction == Direction.RIGHT:
                self.image = pygame.transform.rotate(self.image, 180.0)
            elif  direction == Direction.UP:
                self.image = pygame.transform.rotate(self.image, -90.0)
            elif   direction == Direction.DOWN:
                self.image = pygame.transform.rotate(self.image, 90.0)
        elif self.direction == Direction.DOWN:
            if direction == Direction.LEFT:
                self.image = pygame.transform.rotate(self.image, -90.0)
            elif  direction == Direction.UP:
                self.image = pygame.transform.rotate(self.image, 180.0)
            elif direction == Direction.RIGHT:
                self.image = pygame.transform.rotate(self.image, 90.0)
        self.direction = direction
        
    def fallBack(self):
       self.rect = self.old_pos

        
    def move(self, x, y):
        self.old_pos = self.rect
        todel = self.rect
        todel.size = (100, 100)
        self.playground.screen.blit(self.playground.background, todel, todel)
        self.rect = self.rect.move(x, y)
        

    def update(self):
        if not self.cmdFIFO.empty():
            cmd = self.cmdFIFO.get()
            if None != cmd:
                print("update Sprite")
                cmd()
            
    def up(self):
        self.rotate(Direction.UP)
        self.move(0, -50)
        
    def down(self):
        self.rotate(Direction.DOWN)
        self.move(0, 50)
        
    def right(self):
        self.rotate(Direction.RIGHT)
        self.move(50, 0)
        
    def left(self):
        self.rotate(Direction.LEFT)
        self.move(-50, 0)
        
    def cmdUp(self):
        self.cmdFIFO.put(self.up())

    def cmdDown(self):
        self.cmdFIFO.put(self.down())

    def cmdRight(self):
        self.cmdFIFO.put(self.right())

    def cmdLeft(self):
        self.cmdFIFO.put(self.left())
