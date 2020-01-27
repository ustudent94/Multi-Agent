import math, pygame, random
from Assn2.Constant import *


class Dirt:

    def __init__(self):
        self.amount = random.randint(0, CELLWIDTH - 1) % 3 + 1
        self.gone = False
        self.color = self.getColor()
        self.coord = self.newLocation()

    def getColor(self):
        color = BGCOLOR
        if(self.amount == 3):
            color = DARKBROWN
        elif(self.amount == 2):
             color = MIDBROWN
        elif(self.amount == 1):
            color = LIGHTBROWN
        return color

    def getCoord(self):
        return self.coord
    #initializes coordinates
    def newLocation(self):
        self.coord = {'x': random.randint(0, CELLWIDTH - 2), 'y': random.randint(0, CELLHEIGHT - 2)}
        return self.coord

    def suckDirt(self):
        if(self.amount > 1):
            self.amount = self.amount -1
        else:
            self.amount = 0
            self.gone = True

        self.color = self.getColor()

    def ifGone(self):
        return self.gone

    def hit(self, coord):
        hit = False
        if coord == self.coord:
            hit = True
        return hit
    #draws self
    def drawSelf(self):
        x = self.coord['x'] * CELLSIZE
        y = self.coord['y'] * CELLSIZE
        xcenter = self.coord['x'] * CELLSIZE + math.floor(CELLSIZE / 2)
        ycenter = self.coord['y'] * CELLSIZE + math.floor(CELLSIZE / 2)
        pygame.draw.circle(DISPLAYSURF, self.color, (xcenter, ycenter), RADIUS)
