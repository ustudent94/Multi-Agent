import pygame, random
from pygame.constants import *

#import constants
from Assn1.Constant import CELLWIDTH, CELLHEIGHT, CELLSIZE, RIGHT, LEFT, UP, DOWN, HEAD, WHITE


#Worm class
class Worm:

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
    def getCoord(self):
        return self.wormCoords

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
        if (event.key == self.leftKey or event.key == K_KP4) and self.direction != RIGHT:
            self.direction = LEFT
        elif (event.key == self.rightKey or event.key == K_KP6) and self.direction != LEFT:
            self.direction = RIGHT
        elif (event.key == self.upKey or event.key == K_KP8) and self.direction != DOWN:
            self.direction = UP
        elif (event.key == self.downKey or event.key == K_KP2) and self.direction != UP:
            self.direction = DOWN

    #test hit self
    def hitSelf(self):
        hit = False
        for wormBody in self.wormCoords[1:]:
            if wormBody['x'] == self.wormCoords[HEAD]['x'] and wormBody['y'] == self.wormCoords[HEAD]['y']:
                return True# game over
        return hit

    def hitEdge(self):
        return self.wormCoords[HEAD]['x'] == -1 or self.wormCoords[HEAD]['x'] == CELLWIDTH or self.wormCoords[HEAD]['y'] == -1 or self.wormCoords[HEAD]['y'] == CELLHEIGHT

    #todo: test this with similar coordinate such as apple
    #test hit other snake
    #@param coordList: the wormCoords of the other snake you want to check against
    def hitObject(self, coordList):
        hit = False
        for block in coordList:
            if block['x'] == self.wormCoords[HEAD]['x'] and block['y'] == self.wormCoords[HEAD]['y']:
                return True # game over\
        return hit

    #test hit apple
    #@param apple: Apple coordinates
    def ateApple(self,apple):
        if self.wormCoords[HEAD]['x'] == apple['x'] and self.wormCoords[HEAD]['y'] == apple['y']:
            return True
        else:
            return False

    def removeTail(self):
        del self.wormCoords[-1]  # remove worm's tail segment

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

    def drawScore(self, BASICFONT,DISPLAYSURF):
        score = self.getScore()
        scoreSurf = BASICFONT.render('Score ' + str(self.id) + ': %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = ((self.id -1)*120, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

    def containsKey(self,key):
        if key == self.upKey or key == self.downKey or key == self.rightKey or key == self.leftKey:
            return True
        else:
            return False