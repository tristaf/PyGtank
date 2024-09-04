import pygame
import os

from Classes.PyGSprite import PyGSprite

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1800


IMG_PATH="img/explosion"

class Explosion(pygame.sprite.Sprite):

    HEIGHT = 256
    WIDTH = 256
    
    def __init__(self, center, playground):
        pygame.sprite.Sprite.__init__(self)
        self.playground = playground
        self.images = []
        self.animation_frame = 0
        for index in range(9):
            filename = "Explosion" + str(index) + ".png"
            image = pygame.image.load(os.path.join(IMG_PATH, filename)).convert_alpha()
            self.images.append(image)
            self.animation_frame += 1
        self.rect = pygame.Rect(0, 0, Explosion.WIDTH, Explosion.HEIGHT)
        self.rect.center = center
        self.current_frame = 0
        self.index = 0
        self.image = self.images[self.index]
        
        
    def update(self):
        self.current_frame += 1
        if self.index != 8:
            if self.current_frame > self.animation_frame:
                self.current_frame = 0
                self.index = (self.index + 1) % len(self.images)
                todel = self.rect
                todel.size = (300, 300)
                self.playground.screen.blit(self.playground.background, todel, todel)
                self.image = self.images[self.index]

    
                
        
