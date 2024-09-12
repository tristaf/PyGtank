import pygame

from Classes.PyGSprite import PyGSprite

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1800

IMG = 'player.png'

class Player(PyGSprite):

    HEIGHT = 81
    WIDTH = 100
    
    def __init__(self):
        PyGSprite.__init__(self, IMG, 50, (SCREEN_HEIGHT - Player.HEIGHT) / 2)

   
