import pygame

from Classes.BaseSprite import BaseSprite
from Classes.LayerSprite import LayersSprite

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1800

IMG_BODY = 'player_body.png'
IMG_GUN = 'player_gun.png'

class Player(LayersSprite):

    HEIGHT = 82
    WIDTH = 100
    
    def __init__(self, posX, posY):
        LayersSprite.__init__(self)
        self.addLayer("body", BaseSprite(IMG_BODY, posX, posY))
        self.addLayer("gun", BaseSprite(IMG_GUN, posX, posY))
        

   
