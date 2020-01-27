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
        self.rotDir = 1 # only based on positive or negative directions up,right + left,right -
        #-1 clockwise 1 clockwise direction
        self.direction = direction
        self.dirNum = self.getDirNum()
        self.charger = Charger(id)
        self.batteryLife = 200
        self.disabled = False
        self.coords = self.charger.getCoord() #self.charger.getCoord()
        self.maxDirt = 0
        self.loopStartCoord = self.coords
        self.loopNum = 0
        self.finishedExteriorLoop = False
        self.WAC = 0 # wallAvoidCount
        self.OAC = 0 # objectAvoidCount



    def getId(self):
        return self.id

    def getColor(self):
        return self.color

    def getDirection(self):
        return self.direction

    def getDirNum(self):
        counter = 0
        found = False
        for dir in DIRECTIONS:
            if(not found):
                found = self.direction == dir
                if(not found):
                    counter = counter + 1
        return counter

    def getCoord(self):
        return self.coords

    #Enter -1 or 1 for @param rotdir to look at the cell to the left or right of the rommba respectively
    def getNext(self, rotDir = 0):
        direction = DIRECTIONS[(self.dirNum + rotDir) % 4]
        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': self.coords['x'], 'y': self.coords['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': self.coords['x'], 'y': self.coords['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': self.coords['x'] - 1, 'y': self.coords['y']}
        elif direction == RIGHT:
             newHead = {'x': self.coords['x'] + 1, 'y': self.coords['y']}
        return newHead

    def setDirection(self, direction):
        self.direction = direction

    def setDir(self, num):
        self.direction = DIRECTIONS[num]
        self.dirNum = self.getDirNum()

    def foundDirt(self):
        return self.maxDirt > 0

    #initializes worm coordinates
    def resetCoords(self):
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        self.coords = [{'x': startx, 'y': starty}]

    #test if worm has hit edge
    def hitEdge(self):
        hit = False
        if self.coords['x'] <= 1 + self.loopNum and self.direction == LEFT:
            hit = True
        if self.coords['x'] >= CELLWIDTH-2 -self.loopNum and self.direction == RIGHT:
            hit = True
        if self.coords['y'] <= 1+ self.loopNum and self.direction == UP:
            hit = True
        if self.coords['y'] >= CELLHEIGHT-2-self.loopNum and self.direction == DOWN:
            hit = True
        if hit:
            self.setWAC()
        return hit

    def setWAC(self):
        if(self.WAC==1):
            self.setDir((self.dirNum + self.rotDir) % 4)
        self.WAC = 2
        self.changeRotDir()
        #self.moveSelf()

    def nextLoop(self):
        self.loopNum = self.loopNum + 1
        self.coords['x'] = self.coords['x'] + 1
        self.coords['y'] = self.coords['y'] + 1

    #test hit other snake
    #@param coordList: the coordinates of the other object you want to check against
    def hitObject(self, coordList):
        hit = False
        for block in coordList:
            if block['x'] == self.coords['x'] and block['y'] == self.coords['y']:
                self.OAC = 2
                return True # game over\
        return hit

    #removes last segment of self
    def removeTail(self):
        del self.coords[-1]  # remove worm's tail segment

    def moveSelf(self):
        #self.avoid() # changes direction if obstacle was found needed
        if(not self.disabled):
            self.coords = self.getNext()  #have already removed the last segment
        self.disabled = False
        #move diagonally to the start of next loop
        if(self.coords == self.loopStartCoord):
             self.shiftLoop()
    #this assumes nothing is in the way
    def shiftLoop(self):
        if (not self.foundDirt()):
            self.finishedExteriorLoop = True
            self.rotate(1)
            self.moveSelf()
            self.rotate(1)
            self.moveSelf()
            self.rotate(-1)
            self.loopStartCoord = self.coords
            self.loopNum = self.loopNum + 1
        self.maxDirt = 0

    #draws the bullet
    def drawSelf(self):
        x = self.coords['x'] * CELLSIZE
        y = self.coords['y'] * CELLSIZE
        xcenter = self.coords['x'] * CELLSIZE + math.floor(CELLSIZE / 2)
        ycenter = self.coords['y'] * CELLSIZE + math.floor(CELLSIZE / 2)
        pygame.draw.circle(DISPLAYSURF, self.color, (xcenter, ycenter), RADIUS)
        self.charger.drawSelf()

    def avoid(self):
        # move the worm by adding a segment in the direction it is moving
        if(self.WAC >0):
            self.setDir((self.dirNum + self.rotDir) % 4) #shift direction
            self.WAC = self.WAC-1

        if(self.OAC == 2):
            self.setDir((self.dirNum + self.rotDir) % 4)
            self.OAC = self.OAC  + self.rotDir
        elif(self.OAC ==1):
            self.setDir((self.dirNum - self.rotDir) % 4)
            self.OAC = self.OAC - self.rotDir

    def rotate(self,rotDir = 0):
        if rotDir == 0:
            rotDir = self.rotDir
        self.setDir((self.dirNum + rotDir) % 4)  # shift direction

    def changeRotDir(self):
        if self.rotDir == -1:
            self.rotDir = 1
        else:
            self.rotDir = -1


    # def changeDirection(self):
    #     direction = DIRECTIONS[random.randint(5, CELLWIDTH - 6) % 4]
    #     while direction == self.direction:
    #         direction = DIRECTIONS[random.randint(5, CELLWIDTH - 6) % 4]
    #     self.direction = direction
    #     return direction
