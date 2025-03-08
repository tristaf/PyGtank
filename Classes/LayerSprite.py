class LayersSprite(object):
    def __init__(self):
        self.sprites = {}
        self.layers = []

    def addLayer(self, name, sprite):
        self.sprites[name] = sprite
        self.layers.append(name)

    def getLayer(self, name):
        return self.sprites[name]
        
    def cmdRotate(self, name, angle):
        self.sprites[name].rotate(angle)
        

    def cmdUp(self):
        for layer in self.layers:
            self.sprites[layer].cmdUp()

    def cmdDown(self):
        for layer in self.layers:
            self.sprites[layer].cmdDown()

    def cmdRight(self):
        for layer in self.layers:
             self.sprites[layer].cmdRight()

    def cmdLeft(self):
        for layer in self.layers:
            self.sprites[layer].cmdLeft()

    def fallBack(self):
        for layer in self.layers:
            self.sprites[layer].fallBack()

    def addToSpriteGroup(self, group):
        for layer in self.layers:
            group.add(self.sprites[layer])
    
    def removeFromSpriteGroup(self, group):
        for layer in self.layers:
            group.remove(self.sprites[layer])
