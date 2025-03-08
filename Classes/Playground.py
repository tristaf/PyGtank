import pygame
import os
import sys


from Classes.Explosion import Explosion



IMG_PATH="img"
BACK_IMG = "back.png"

class Playground:
     def __init__(self):
          from Classes.Context import Context
          self.context = Context()
          #self.player = self.context.player
         


     def init(self):
          self.playerGroup = self.context.playerGroup
          self.player = self.context.player
          self.obstacles = self.context.obstaclesGroup
          self.sprites = self.context.spritesGroup
          self.mines = self.context.minesGroup
          self.enemies = self.context.enemiesGroup
          self.screen = self.context.screen
          self.clock = pygame.time.Clock()
          self.background = pygame.image.load(os.path.join(IMG_PATH, BACK_IMG)).convert()
          self.context.screen.blit(self.background, (0,0))

     def linkServer(self, server):
          self.server = server

       
     def run(self):
          while True:
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         self.server.kill()
                         sys.exit()
               
               
               list_obstacles = pygame.sprite.groupcollide(self.playerGroup, self.obstacles, False, False)
               if list_obstacles:
                    self.server.stopMoves()
                    self.player.fallBack()
               else:
                    self.sprites.draw(self.screen)
                    

               mine = pygame.sprite.groupcollide(self.playerGroup, self.mines, True, True)
               
               enemie = pygame.sprite.groupcollide(self.playerGroup, self.enemies, True, True)
               
               if mine or enemie:
                    self.server.stopMoves()
                    self.player.fallBack()
                    self.player.removeFromSpriteGroup(self.sprites)
                    self.sprites.add(Explosion(self.player.getLayer("body").rect.center))
               else:
                    self.sprites.draw(self.screen)
                    
                    
               self.sprites.update()
               pygame.display.update()
               
               self.clock.tick(60)    


'''
     def run(self):
          while True:
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         self.server.kill()
                         sys.exit()
               self.sprites.draw(self.screen)
               self.sprites.update()
               for sprite in self.player:
                    sprite.printName()
               pygame.display.update()
               
               self.clock.tick(60) 

'''  
