import pygame, random
from pygame.constants import *

#import constants
from Assn1.wormy import CELLWIDTH, CELLHEIGHT, CELLSIZE, RIGHT, LEFT, UP, DOWN, HEAD


#Worm class
class worm:

    def __init__(self, id, upKey, downKey, rightKey, leftKey, color, direction):
        self.id = id

        #directional keys
        self.upKey = upKey
        self.downKey = downKey
        self.rightKey = rightKey
        self.leftKey = leftKey

        self.color = color
        self.direction = direction
        self.resetWormCoords()

    def getId(self):
        return self.id
    def getUp(self):
        return self.upKey
    def getDown(self):
        return self.downKey
    def getRight(self):
        return self.rightKey
    def getLeft(self):
        return  self.leftKey
    def getColor(self):
        return self.color

    def getDirection(self):
        return self.direction
    def getScore(self):
        return len(self.wormCoords) - 3

    def setDirection(self, direction):
        self.direction = direction

    def resetWormCoords(self):
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        self.wormCoords = [{'x': startx, 'y': starty},
                             {'x': startx - 1, 'y': starty},
                             {'x': startx - 2, 'y': starty}]

    def eventHandler(self,event):
        #number pad is constant and will work for any worm on the board
        if (event.key == self.leftKey or event.key == K_a) and self.direction != RIGHT:
            direction = self.leftKey
        elif (event.key == self.rightKey or event.key == K_d) and self.direction != LEFT:
            direction = RIGHT
        elif (event.key == self.upKey or event.key == K_w) and self.direction != DOWN:
            direction = UP
        elif (event.key == self.downKey or event.key == K_s) and self.direction != UP:
            direction = DOWN

    #test hit self
    def hitObject(self):
        hit = False
        for wormBody in self.wormCoords[1:]:
            if wormBody['x'] == self.wormCoords[HEAD]['x'] and wormBody['y'] == self.wormCoords[HEAD]['y']:
                return True# game over
        return hit

    #todo: test this with similar coordinate such as apple
    #test hit other snake
    #@param coordList: the wormCoords of the other snake you want to check against
    def hitObject(self, coordList):
        hit = False
        for block in coordList:
            if block['x'] == coordList[HEAD]['x'] and block['y'] == coordList[HEAD]['y']:
                return True # game over\
        return hit

    #test hit apple
    #@param apple: Apple coordinates
    def ateApple(self,apple):
        if self.wormCoords[HEAD]['x'] == apple['x'] and self.wormCoords[HEAD]['y'] == apple['y']:
            apple = apple.newLocation() # set a new apple somewhere
            return True
        else:
            del self.wormCoords[-1]  # remove worm's tail segment
            return False

    def moveWorm(self):
        # move the worm by adding a segment in the direction it is moving
        if self.direction == UP:
            newHead = {'x': self.wormCoords[HEAD]['x'], 'y': self.wormCoords[HEAD]['y'] - 1}
        elif self.direction == DOWN:
            newHead = {'x': self.wormCoords[HEAD]['x'], 'y': self.wormCoords[HEAD]['y'] + 1}
        elif self.direction == LEFT:
            newHead = {'x': self.wormCoords[HEAD]['x'] - 1, 'y': self.wormCoords[HEAD]['y']}
        elif self.direction == RIGHT:
            newHead = {'x': self.wormCoords[HEAD]['x'] + 1, 'y': self.wormCoords[HEAD]['y']}
        self.wormCoords.insert(0, newHead)   #have already removed the last segment

    def drawWorm(self, DISPLAYSURF):
        for coord in self.wormCoords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(DISPLAYSURF, self.color, wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(DISPLAYSURF, self.color, wormInnerSegmentRect)
