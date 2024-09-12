#!/usr/bin/python3

import pygame
import os
import sys
import random

from Classes.Context import Context
from Classes.Enemy import Enemy
from Classes.Player import Player
from Classes.Stone import Stone
from Classes.Mine import Mine
from Classes.Playground import Playground
from Classes.Direction import Direction
from Classes.TankServer import TankServer
from Classes.Explosion import Explosion



SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1800
NB_ENEMY = 3
NB_OBSTACLES = 2
NB_MINES = 0

PORT_NUM = 4242


def main():             
    screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    context = Context()
    context.setScreen(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    playground = Playground()
    context.setPlayground(playground)
    
    player = Player()
    context.addPlayer(player)
    context.addSprite(player)


    #explosion = Explosion((SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2), playground)
    #allSprites.add(explosion)
    
    for y in range(1, NB_ENEMY + 1):
        enemy = Enemy(1600, ((SCREEN_HEIGHT - NB_ENEMY * Enemy.HEIGHT) / (NB_ENEMY + 1)) * y  + Enemy.HEIGHT * ( y - 1))
        context.addEnemy(enemy)
        context.addSprite(enemy)
    
    for y in range(1, NB_OBSTACLES + 1):
        stone = Stone(SCREEN_WIDTH / 2 + 10, ((SCREEN_HEIGHT - NB_OBSTACLES * Stone.SIZE) / (NB_OBSTACLES + 1)) * y  + Stone.SIZE * ( y - 1))
        context.addObstacle(stone)
        context.addSprite(stone)
   

    for i in range(0, NB_MINES - 1):
        mine = Mine(400 + random.randrange(SCREEN_WIDTH - 400), 100 + random.randrange(SCREEN_HEIGHT - 200))
        context.addMine(mine)
        context.addSprite(mine)
    mine = Mine(1200 , SCREEN_HEIGHT / 2 - 200)
    context.addMine(mine)
    context.addSprite(mine)
    
    TankServer('', PORT_NUM).start()
    playground.init()
    playground.run()
'''

def main():             
    screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    context = Context()
    context.setScreen(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    playground = Playground()
    context.setPlayground(playground)
    
    player = Player("titi")
    context.addPlayer(player)
    context.addSprite(player)

    TankServer('', PORT_NUM, playground).start()
    playground.run()
'''

     

                   
    

if __name__ == '__main__':
    main()
