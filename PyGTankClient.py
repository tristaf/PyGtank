#!/usr/bin/python3

import socket

from Classes.Tank import Tank
 
def Main():
    tank = Tank()
    tank.start()

   
    
    for i in range(10):
        tank.right()

    #tank.rotateGun()
        
    #for i in range(13):
    #    tank.right()    

    for i in range(10):
        tank.right() 
    
    for i in range(5):
        tank.up()
    
    for i in range(9):
        tank.down()

    for i in range(10):
        tank.right()    
     
        
    tank.end()
    
 
if __name__ == '__main__':
    Main()
