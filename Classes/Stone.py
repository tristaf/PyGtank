import pygame
from Classes.Context import Context

IMG = 'stone.png'

from Classes.BaseSprite import BaseSprite 
from Classes.LayerSprite import LayersSprite

class Stone(LayersSprite):

    SIZE = 64
    
    def __init__(self, posX, posY):
        LayersSprite.__init__(self)
        self.addLayer("stone", BaseSprite(IMG , posX, posY))
        
