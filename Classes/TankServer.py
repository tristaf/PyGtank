import socket
import threading

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


    def parse(self, request):
        commands = request.split(';')
        for cmd in commands:
            if self.stop:
                break;
            print(cmd)            
            if "up" == cmd:
                self.player.up()
            elif "down" == cmd:
                self.player.down()
            elif "right" == cmd:
                self.player.right()
            elif "left" == cmd:
                self.player.left()
        self.stop = False
        
    def stopMoves(self):
        self.stop = True
            
    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            #client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    self.parse(data.decode('ascii'))
                    client.send("Ok".encode('ascii'))
                else:
                    raise error('Client disconnected')
            except RuntimeError as error:
                print(error)
                return False

    def start(self):
         threading.Thread(target = self.listen).start()
