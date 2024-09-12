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
          self.player = self.context.player.sprites()[0]
          self.obstacles = self.context.obstacles
          self.sprites = self.context.sprites
          self.mines = self.context.mines
          self.enemies = self.context.enemies
          self.obstacles =  self.context.obstacles
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
                    self.sprites.add(Explosion(self.player.rect.center))
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
