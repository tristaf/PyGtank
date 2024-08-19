#!/usr/bin/python3

import socket
import threading 
 
class Tank():
    HOST = '127.0.0.1'
    PORT = 4242

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((Tank.HOST, Tank.PORT))
        self.send = False
        self.command  = ''
        self.commands = []
        
    def sendCmd(self):    
        while True:
            if self.send:
                self.socket.send(self.command.encode('ascii'))
                self.response = self.socket.recv(1024)
                self.send = False
        self.socket.close()

    
    def start(self):
         threading.Thread(target = self.sendCmd).start()
        
        
    def up(self):
        self.commands.append('up')

    def down(self):
        self.commands.append('down')

    def right(self):
        self.commands.append('right')

    def left(self):
        self.commands.append('left')

    def end(self):
        self.command = ';'.join(self.commands)
        self.send = True
