#!/usr/bin/python3

import pygame
import os
import sys
import random


from Classes.Enemy import Enemy
from Classes.Player import Player
from Classes.Stone import Stone
from Classes.Mine import Mine
from Classes.Playground import Playground
from Classes.Direction import Direction
from Classes.TankServer import TankServer



SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1800
NB_ENEMY = 3
NB_OBSTACLES = 4
NB_MINES = 5

PORT_NUM = 4242


def main():             
    screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    playground = Playground(SCREEN_WIDTH, SCREEN_HEIGHT, screen)

    player = Player(playground)
    playground.addPlayer(player)

    allSprites = pygame.sprite.Group()
    allSprites.add(player)
    
    enemies = pygame.sprite.Group()
    for y in range(1, NB_ENEMY + 1):
        enemy = Enemy(1600, ((SCREEN_HEIGHT - NB_ENEMY * Enemy.HEIGHT) / (NB_ENEMY + 1)) * y  + Enemy.HEIGHT * ( y - 1), playground)
        enemies.add(enemy)
        allSprites.add(enemy)
    playground.addEnemies(enemies)
    
    stones = pygame.sprite.Group()
    for y in range(1, NB_OBSTACLES + 1):
        stone = Stone(SCREEN_WIDTH / 2 + 10, ((SCREEN_HEIGHT - NB_OBSTACLES * Stone.SIZE) / (NB_OBSTACLES + 1)) * y  + Stone.SIZE * ( y - 1), playground)
        stones.add(stone)
        allSprites.add(stone)
    playground.addObstacles(stones)

    mines =  pygame.sprite.Group()
    for i in range(0, NB_MINES):
        mine = Mine(400 + random.randrange(SCREEN_WIDTH - 400), 100 + random.randrange(SCREEN_HEIGHT - 200), playground)
        mines.add(mine)
        allSprites.add(mine)
    
    playground.addSprites(allSprites)
    
    TankServer('', PORT_NUM, playground).start()
    playground.run()
   
     

                   
    

if __name__ == '__main__':
    main()
