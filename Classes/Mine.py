import pygame

IMG = 'mine.png'

from Classes.BaseSprite import BaseSprite 
from Classes.LayerSprite import LayersSprite

class Mine(LayersSprite):
    def __init__(self, posX, posY):
        LayersSprite.__init__(self)
        self.addLayer("mine", BaseSprite(IMG , posX, posY))
