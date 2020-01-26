import math, pygame, random
from Assn1.Constant import CELLSIZE, RED, RADIUS, CELLHEIGHT, CELLWIDTH


class Dirt:

    def __init__(self,id,color = RED,):
        self.id = id
        self.color = color
        self.coord = self.newLocation()


    def getId(self):
        return self.id

    def getColor(self):
        return self.color

    def getCoord(self):
        return self.coord
    #initializes coordinates
    def newLocation(self):
        self.coord = {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
        return self.coord
    #draws the apple
    def drawApple(self,DISPLAYSURF):
        x = self.coord['x'] * CELLSIZE
        y = self.coord['y'] * CELLSIZE
        xcenter = self.coord['x'] * CELLSIZE + math.floor(CELLSIZE / 2)
        ycenter = self.coord['y'] * CELLSIZE + math.floor(CELLSIZE / 2)
        # appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        # pygame.draw.rect(DISPLAYSURF, RED, appleRect)
        pygame.draw.circle(DISPLAYSURF, RED, (xcenter, ycenter), RADIUS)

    # #FOR DEBUG ONLY
    # def newLocation(self):
    #     if self.id == 1:
    #         self.location = {'x': 7, 'y': 3}
    #     if self.id == 2:
    #         self.location = {'x': 10, 'y': 8}
    #     return self.location