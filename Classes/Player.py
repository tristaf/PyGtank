import pygame

from Classes.PyGSprite import PyGSprite

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1800


class Player(PyGSprite):

    HEIGHT = 81
    WIDTH = 100
    
    def __init__(self, playground):
        PyGSprite.__init__(self, 'player.png', 50, (SCREEN_HEIGHT - Player.HEIGHT) / 2, playground)
