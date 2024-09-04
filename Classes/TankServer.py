import socket
import threading
import pygame

from Classes.Player import Player

class TankServer(object):
    def __init__(self, host, port, playground):
        print("Init tank server");
        self.player = playground.player
        playground.linkServer(self)
        self.stop = False
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.loopValue = True


    def parse(self, request):
        commands = request.split(';')
        for cmd in commands:
            if self.stop:
                break;
            #print(cmd)            
            if "up" == cmd:
                self.player.cmdUp()
            elif "down" == cmd:
                self.player.cmdDown()
            elif "right" == cmd:
                self.player.cmdRight()
            elif "left" == cmd:
                self.player.cmdLeft()
            pygame.time.wait(500)
        self.stop = False
        
    def stopMoves(self):
        self.stop = True
            
    def listen(self):
        self.sock.listen(5)
        while  self.loopValue:
            client, address = self.sock.accept()
            #client.settimeout(60)
            self.thread2 = threading.Thread(target = self.listenToClient, args = (client,address))
            self.thread2.start()
        print("Stop listen1")
        self.thread2.join()
        print("Stop listen2")

    def listenToClient(self, client, address):
        size = 1024
        while  self.loopValue:
            
            try:
                data = client.recv(size)
                if data:
                    self.parse(data.decode('ascii'))
                    client.send("Ok".encode('ascii'))
                else:
                    raise Exception('Client disconnected')
            except RuntimeError as error:
                print(error)
                return False
        client.close()
        print("Stop listenToClient")
        
    def start(self):
         self.thread1 = threading.Thread(target = self.listen)
         self.thread1.start()

    def kill(self):
        self.loopValue = False
        self.thread1.join()
        
