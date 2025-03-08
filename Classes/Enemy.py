import pygame
from Classes.Context import Context

IMG = 'enemy.png'

from Classes.BaseSprite import BaseSprite 
from Classes.LayerSprite import LayersSprite

class Enemy(LayersSprite):

    WIDTH = 100
    HEIGHT = 62
    
    def __init__(self, posX, posY):
        LayersSprite.__init__(self)
        self.addLayer("enemy", BaseSprite(IMG , posX, posY))
        
