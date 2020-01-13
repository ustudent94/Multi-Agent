import math, pygame
from Assn1.wormy import CELLSIZE, RED, RADIUS


class Apple:

    def __init__(self,id,color = RED,):
        self.id = id
        self.color = color

    def getId(self):
        return self.id

    def getColor(self):
        return self.color

    def drawApple(coord,DISPLAYSURF):
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        xcenter = coord['x'] * CELLSIZE + math.floor(CELLSIZE / 2)
        ycenter = coord['y'] * CELLSIZE + math.floor(CELLSIZE / 2)
        # appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        # pygame.draw.rect(DISPLAYSURF, RED, appleRect)
        pygame.draw.circle(DISPLAYSURF, RED, (xcenter, ycenter), RADIUS)