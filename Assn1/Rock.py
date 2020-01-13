from Assn1.Constant import *
import pygame

class Rock:

    def __init__(self,coords):
        self.coords = coords

    def getCoord(self):
        return self.coords

    def isEmpty(self):
        return len(self.coords) == 0

    def drawRock(self, DISPLAYSURF):
        for coord in self.coords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(DISPLAYSURF, GREY, wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(DISPLAYSURF, GREY, wormInnerSegmentRect)