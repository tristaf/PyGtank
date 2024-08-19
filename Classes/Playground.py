import pygame
import os
import sys

IMG_PATH="img"
BACK_IMG = "back.png"

class Playground:
     def __init__(self, height, width, screen):
         self.screen = screen
         self.clock = pygame.time.Clock()
         self.background = pygame.image.load(os.path.join(IMG_PATH, BACK_IMG)).convert()
         self.screen.blit(self.background, (0,0))

     def addPlayer(self, player):
         self.player = player

     def addEnemies(self, enemies):
         self.enemies = enemies

     def addObstacles(self, obstacles):
         self.obstacles = obstacles

     def addSprites(self, spritess):
         self.sprites = spritess

     def linkServer(self, server):
          self.server = server
    
         
     def run(self):
          while True:
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         sys.exit()
               
               list_obstacles = pygame.sprite.spritecollide(self.player, self.obstacles, False)
               if list_obstacles:
                    self.server.stopMoves()
                    self.player.fallBack()
               else:
                    self.sprites.draw(self.screen)
               
               pygame.display.update()
               
               self.clock.tick(10)    
