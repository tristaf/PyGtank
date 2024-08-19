import pygame

IMG = 'stone.png'

from Classes.PyGSprite import PyGSprite 

class Stone(PyGSprite):

    SIZE = 64
    
    def __init__(self, posX, posY, playground):
        PyGSprite.__init__(self, IMG , posX, posY, playground)
