import pygame

IMG = 'mine.png'

from Classes.BaseSprite import BaseSprite 

class Mine(BaseSprite):
    def __init__(self, posX, posY):
        BaseSprite.__init__(self,IMG , posX, posY)
