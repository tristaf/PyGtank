import pygame
from Classes.Singleton import Singleton
from Classes.Playground import Playground

	
class Context(object, metaclass=Singleton):
    def __init__(self):
        self.spritesGroup = pygame.sprite.Group()
        self.enemiesGroup = pygame.sprite.Group()
        self.enemies = []
        self.playerGroup = pygame.sprite.Group()
        self.player = None
        self.minesGroup = pygame.sprite.Group()
        self.obstaclesGroup = pygame.sprite.Group()
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
         obstacle.addToSpriteGroup(self.obstaclesGroup)

    def addMine(self, mine):
         mine.addToSpriteGroup(self.minesGroup)

    def addSprite(self, sprite):
         sprite.addToSpriteGroup(self.spritesGroup)
