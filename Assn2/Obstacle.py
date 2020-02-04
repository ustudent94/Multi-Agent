from Assn2.Constant import *
import pygame, random

class Obstacle:

    def __init__(self, numSegments, direction, startX, startY,type):

        self.direction = direction
        self.coords = [{'x': startX, 'y': startY}]
        i = 0
        while(i < numSegments - 1):
            self.addSegments()
            i = i +1
        self.type = type

        if(type == 'furniture'):
            self.color = BLUE
        elif(type == 'drop'):
            self.color = BGCOLOR
        else:
            #otherwise generic obstacle
            self.color = YELLOW

    def getCoord(self):
        return self.coords


    #draws self
    def drawSelf(self):
        for coord in self.coords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            Rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(DISPLAYSURF, RED, Rect)
            innerRect = pygame.Rect(x + 2, y + 2, CELLSIZE - 4, CELLSIZE - 4)
            pygame.draw.rect(DISPLAYSURF, self.color, innerRect)

    def addSegments(self):
        # move the wall by adding a segment in the direction it is moving
        if self.direction == UP:
            newBlock = {'x': self.coords[-1]['x'], 'y': self.coords[-1]['y'] - 1}
        elif self.direction == DOWN:
            newBlock = {'x': self.coords[-1]['x'], 'y': self.coords[-1]['y'] + 1}
        elif self.direction == LEFT:
            newBlock = {'x': self.coords[-1]['x'] - 1, 'y': self.coords[-1]['y']}
        elif self.direction == RIGHT:
            newBlock = {'x': self.coords[-1]['x'] + 1, 'y': self.coords[-1]['y']}
        self.coords.append(newBlock)

    def hit(self, coord):
        hit = False
        for block in self.coords:
            if block == coord:
                hit = True
        return hit

