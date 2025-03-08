import pygame
from Classes.Singleton import Singleton
from Classes.Playground import Playground
from Classes.BaseSprite import BaseSprite
from Classes.LayersSprite import LayersSprite
	
class Context(object, metaclass=Singleton):
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.enemiesGroup = pygame.sprite.Group()
        self.enemies = []
        self.playerGroup = pygame.sprite.Group()
        self.player = None
        self.mines = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.playground:Playground = None 

    def setScreen(self, height, width, screen):
        self.screen = screen
        self.screenHeight = height
        self.screenWidth = width

    def setPlayground(self, playground):
        self.playground = playground

    def addPlayer(self, player):
         player.addToSpriteGroup(self.playerGroup)
         self.player = player

    def addEnemy(self, enemy):
         enemy.addToSpriteGroup(self.enemiesGroup)
         self.enemies.append(enemy)

    def addObstacle(self, obstacle):
         self.obstacles.add(obstacle)

    def addMine(self, mine):
         self.mines.add(mine)

    def addSprite(self, sprite):
        if isinstance(sprite, LayersSprite):
            sprite.addToSpriteGroup(self.sprites)
        elif isinstance(sprite, BaseSprite):
            self.sprites.add(sprite)
