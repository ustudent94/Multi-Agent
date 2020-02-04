import math, pygame, random
from Assn2.Constant import *


class Charger:

    def __init__(self,id,chargerCoords, color = YELLOW):
        self.id = id
        self.color = color
        self.coords = chargerCoords #{'x': 1, 'y': CELLHEIGHT-2}


    def getId(self):
        return self.id

    def getColor(self):
        return self.color

    def getCoord(self):
        return self.coords

    #draws self
    def drawSelf(self):
        x = self.coords['x'] * CELLSIZE
        y = self.coords['y'] * CELLSIZE
        Rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, self.color, Rect)
        innerRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, self.color, innerRect)