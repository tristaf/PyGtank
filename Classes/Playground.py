import pygame
import os
import sys

from Classes.Explosion import Explosion

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

     def addMines(self, mines):
         self.mines = mines

     def addSprites(self, sprite):
         self.sprites = sprite

     def linkServer(self, server):
          self.server = server
    
         
     def run(self):
          while True:
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         self.server.kill()
                         sys.exit()
               
               list_obstacles = pygame.sprite.spritecollide(self.player, self.obstacles, False)
               if list_obstacles:
                    self.server.stopMoves()
                    self.player.fallBack()
               else:
                    self.sprites.draw(self.screen)
                    
               explosion = pygame.sprite.spritecollide(self.player, self.mines, True)

               enemie = pygame.sprite.spritecollide(self.player, self.enemies, True)
               
               if explosion or enemie:
                    self.server.stopMoves()
                    self.player.fallBack()
                    self.sprites.remove(self.player)
                    self.sprites.add(Explosion(self.player.rect.center, self))
               else:
                    self.sprites.draw(self.screen)
                    
                    
               self.sprites.update()
               pygame.display.update()
               
               self.clock.tick(60)    
