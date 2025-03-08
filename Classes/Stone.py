import pygame
from Classes.Context import Context

IMG = 'stone.png'

from Classes.BaseSprite import BaseSprite 

class Stone(BaseSprite):

    SIZE = 64
    
    def __init__(self, posX, posY):
        BaseSprite.__init__(self, IMG , posX, posY)
        
