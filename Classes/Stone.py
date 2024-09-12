import pygame
from Classes.Context import Context

IMG = 'stone.png'

from Classes.PyGSprite import PyGSprite 

class Stone(PyGSprite):

    SIZE = 64
    
    def __init__(self, posX, posY):
        PyGSprite.__init__(self, IMG , posX, posY)
