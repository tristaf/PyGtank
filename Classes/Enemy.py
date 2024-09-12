import pygame
from Classes.Context import Context

IMG = 'enemy.png'

from Classes.PyGSprite import PyGSprite 

class Enemy(PyGSprite):

    WIDTH = 100
    HEIGHT = 62
    
    def __init__(self, posX, posY):
        PyGSprite.__init__(self, IMG , posX, posY)
        
