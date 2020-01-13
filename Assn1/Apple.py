import math, pygame, random
from Assn1.Constant import CELLSIZE, RED, RADIUS, CELLHEIGHT, CELLWIDTH


class Apple:

    def __init__(self,id,color = RED,):
        self.id = id
        self.color = color
        self.location = self.newLocation()


    def getId(self):
        return self.id

    def getColor(self):
        return self.color

    def getLocation(self):
        return self.location

    def drawApple(self,DISPLAYSURF):
        x = self.location['x'] * CELLSIZE
        y = self.location['y'] * CELLSIZE
        xcenter = self.location['x'] * CELLSIZE + math.floor(CELLSIZE / 2)
        ycenter = self.location['y'] * CELLSIZE + math.floor(CELLSIZE / 2)
        # appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        # pygame.draw.rect(DISPLAYSURF, RED, appleRect)
        pygame.draw.circle(DISPLAYSURF, RED, (xcenter, ycenter), RADIUS)

    def newLocation(self):
        self.location = {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
        return self.location

    #todo: remove after debug
    def newLocation(self):
        if self.id == 1:
            self.location = {'x': 8, 'y': 3}
        if self.id == 2:
            self.location = {'x': 10, 'y': 8}
        return self.location