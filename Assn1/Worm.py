import pygame, random
from pygame.constants import *


#import constants
from Assn1.Constant import CELLWIDTH, CELLHEIGHT, CELLSIZE, RIGHT, LEFT, UP, DOWN, HEAD, WHITE
from Assn1.Bullet import Bullet
from Assn1.Rock import Rock


#Worm class
class Worm:

    def __init__(self, id, upKey, downKey, rightKey, leftKey,fireKey, color, direction):
        self.id = id

        #directional keys
        self.upKey = upKey
        self.downKey = downKey
        self.rightKey = rightKey
        self.leftKey = leftKey
        self.fireKey = fireKey

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

    def getBullet(self):
        return self.bullet

    def getFired(self):
        return self.fired

    def setDirection(self, direction):
        self.direction = direction

    #initializes worm coordinates
    def resetWormCoords(self):
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        self.wormCoords = [{'x': startx, 'y': starty},
                             {'x': startx - 1, 'y': starty},
                             {'x': startx - 2, 'y': starty}]

    # #FOR DEBUG ONLY
    # def resetWormCoords(self):
    #     startx = 5
    #     if self.id == 2:
    #         startx = 10
    #         starty = 10
    #         self.direction = UP
    #
    #     elif self.id == 1:
    #         starty = 3
    #     self.wormCoords = [{'x': startx, 'y': starty},
    #                          {'x': startx - 1, 'y': starty},
    #                          {'x': startx - 2, 'y': starty}]

    #handles key presses given an event
    def eventHandler(self,event):
        self.fired = False
        #number pad is constant and will work for any worm on the board
        if (event.key == self.leftKey or event.key == K_KP4) and self.direction != RIGHT:
            self.direction = LEFT
        elif (event.key == self.rightKey or event.key == K_KP6) and self.direction != LEFT:
            self.direction = RIGHT
        elif (event.key == self.upKey or event.key == K_KP8) and self.direction != DOWN:
            self.direction = UP
        elif (event.key == self.downKey or event.key == K_KP2) and self.direction != UP:
            self.direction = DOWN
        elif (event.key == self.fireKey):
            self.loadBullet()
            self.fired = True

    #test hit self
    def hitSelf(self):
        hit = False
        for wormBody in self.wormCoords[1:]:
            if wormBody['x'] == self.wormCoords[HEAD]['x'] and wormBody['y'] == self.wormCoords[HEAD]['y']:
                return True# game over
        return hit

    #test if worm has hit edge
    def hitEdge(self):
        return self.wormCoords[HEAD]['x'] == -1 or self.wormCoords[HEAD]['x'] == CELLWIDTH or self.wormCoords[HEAD]['y'] == -1 or self.wormCoords[HEAD]['y'] == CELLHEIGHT

    #test hit other snake
    #@param coordList: the coordinates of the other object you want to check against
    def hitObject(self, coordList):
        hit = False
        for block in coordList:
            if block['x'] == self.wormCoords[HEAD]['x'] and block['y'] == self.wormCoords[HEAD]['y']:
                return True # game over\
        return hit
    #test for bullet hit and return to to cut off
    def tailToStone(self, coords):
        hit = False
        rockList = []
        blockNum = 1
        for block in self.wormCoords[1:]:
            if coords['x'] == block['x'] and coords['y'] == block['y']:
                hit = True
            if hit:
                rockList.append(block)
                del self.wormCoords[blockNum]
            else:
                blockNum += 1
        rocks = Rock(rockList)
        return rocks

    #test hit apple
    #@param apple: Apple coordinates
    def ateApple(self,apple):
        if self.wormCoords[HEAD]['x'] == apple['x'] and self.wormCoords[HEAD]['y'] == apple['y']:
            return True
        else:
            return False
    #removes last segment of worm
    def removeTail(self):
        del self.wormCoords[-1]  # remove worm's tail segment

    #adds to the end of worm segments
    def addTail(self):
        # move the worm by adding a segment in the direction it is moving
        if self.direction == DOWN:
            newHead = {'x': self.wormCoords[HEAD]['x'], 'y': self.wormCoords[HEAD]['y'] - 1}
        elif self.direction == UP:
            newHead = {'x': self.wormCoords[HEAD]['x'], 'y': self.wormCoords[HEAD]['y'] + 1}
        elif self.direction == RIGHT:
            newHead = {'x': self.wormCoords[HEAD]['x'] - 1, 'y': self.wormCoords[HEAD]['y']}
        elif self.direction == LEFT:
             newHead = {'x': self.wormCoords[HEAD]['x'] + 1, 'y': self.wormCoords[HEAD]['y']}
        self.wormCoords.append(newHead)   #have already removed the last segment

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
    #given a key returns whether this is one of the active keys for keypresses
    def containsKey(self,key):
        if key == self.upKey or key == self.downKey or key == self.rightKey or key == self.leftKey or key == self.fireKey or key == K_KP2 or key == K_KP4 or key == K_KP6 or key == K_KP8:
            return True
        else:
            return False
    #initializes a bullet to be fired
    def loadBullet(self):
        self.bullet = Bullet(self.direction,self.wormCoords[HEAD])