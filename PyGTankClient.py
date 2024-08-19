#!/usr/bin/python3

import socket

from Classes.Tank import Tank
 
def Main():
    tank = Tank()
    tank.start()

    for i in range(10):
        tank.right()
    for i in range(4):
        tank.up()
    for i in range(20):
        tank.right()
    tank.end()
    
 
if __name__ == '__main__':
    Main()
