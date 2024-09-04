import pygame

IMG = 'mine.png'

from Classes.PyGSprite import PyGSprite 

class Mine(PyGSprite):
    def __init__(self, posX, posY, playground):
        PyGSprite.__init__(self, IMG , posX, posY, playground)
