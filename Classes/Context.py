import pygame
from Classes.Singleton import Singleton
from Classes.Playground import Playground

	
class Context(object, metaclass=Singleton):
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
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
         self.player.add(player)

    def addEnemy(self, enemy):
         self.enemies.add(enemy)

    def addObstacle(self, obstacle):
         self.obstacles.add(obstacle)

    def addMine(self, mine):
         self.mines.add(mine)

    def addSprite(self, sprite):
         self.sprites.add(sprite)
