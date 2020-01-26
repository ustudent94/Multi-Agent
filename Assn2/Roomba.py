import pygame, random, math
from pygame.constants import *
#from random import *


#import constants
from Assn2.Constant import *
from Assn2.Charger import Charger


#Worm class
class Roomba:

    # def __init__(self, id, upKey, downKey, rightKey, leftKey,fireKey, color, direction):
    def __init__(self, id, direction,color = GREY):
        self.id = id

        self.color = color
        self.direction = direction
        self.charger = Charger(id)
        self.batteryLife = 200
        self.coords = [{'x': 1, 'y': 1}]
        self.resetCoords()



    def getId(self):
        return self.id

    def getColor(self):
        return self.color

    def getDirection(self):
        return self.direction

    def getScore(self):
        return len(self.coords) - 3

    def getCoord(self):
        return self.coords

    def getBullet(self):
        return self.bullet

    def getFired(self):
        return self.fired

    def setDirection(self, direction):
        self.direction = direction

    #initializes worm coordinates
    def resetCoords(self):
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        self.coords = [{'x': startx, 'y': starty}]


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

    #test if worm has hit edge
    def hitEdge(self):
        return self.coords[HEAD]['x'] >= 1 or self.coords[HEAD]['x'] >= CELLWIDTH-1 or self.coords[HEAD]['y'] <= 1 or self.coords[HEAD]['y'] >= CELLHEIGHT-1

    #test hit other snake
    #@param coordList: the coordinates of the other object you want to check against
    def hitObject(self, coordList):
        hit = False
        for block in coordList:
            if block['x'] == self.coords[HEAD]['x'] and block['y'] == self.coords[HEAD]['y']:
                return True # game over\
        return hit

    #test hit apple
    #@param apple: Apple coordinates
    def ateApple(self,apple):
        if self.coords[HEAD]['x'] == apple['x'] and self.coords[HEAD]['y'] == apple['y']:
            return True
        else:
            return False
    #removes last segment of roomba
    def removeTail(self):
        del self.coords[-1]  # remove worm's tail segment

    def moveSelf(self):
        # move the worm by adding a segment in the direction it is moving
        if self.direction == UP:
            newHead = {'x': self.coords[HEAD]['x'], 'y': self.coords[HEAD]['y'] - 1}
        elif self.direction == DOWN:
            newHead = {'x': self.coords[HEAD]['x'], 'y': self.coords[HEAD]['y'] + 1}
        elif self.direction == LEFT:
            newHead = {'x': self.coords[HEAD]['x'] - 1, 'y': self.coords[HEAD]['y']}
        elif self.direction == RIGHT:
             newHead = {'x': self.coords[HEAD]['x'] + 1, 'y': self.coords[HEAD]['y']}
        self.coords.insert(0, newHead)   #have already removed the last segment

    #draws the bullet
    def drawSelf(self):
        x = self.coords[HEAD]['x'] * CELLSIZE
        y = self.coords[HEAD]['y'] * CELLSIZE
        xcenter = self.coords[HEAD]['x'] * CELLSIZE + math.floor(CELLSIZE / 2)
        ycenter = self.coords[HEAD]['y'] * CELLSIZE + math.floor(CELLSIZE / 2)
        pygame.draw.circle(DISPLAYSURF, self.color, (xcenter, ycenter), RADIUS)
        self.charger.drawSelf()

    # def drawScore(self, BASICFONT,DISPLAYSURF):
    #     score = self.getScore()
    #     scoreSurf = BASICFONT.render('Score ' + str(self.id) + ': %s' % (score), True, WHITE)
    #     scoreRect = scoreSurf.get_rect()
    #     scoreRect.topleft = ((self.id -1)*120, 10)
    #     DISPLAYSURF.blit(scoreSurf, scoreRect)

    def changeDirection(self):

        direction = DIRECTIONS[random.randint(5, CELLWIDTH - 6) % 4]
        while direction == self.direction:
            direction = DIRECTIONS[random.randint(5, CELLWIDTH - 6) % 4]
        self.direction = direction
        return direction
