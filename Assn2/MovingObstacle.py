from Assn2.Constant import *
import pygame

class MovingObstacle:
    def __init__(self, direction ,coords):
        self.direction = direction
        self.dirNum = self.getDirNum()
        self.coords = coords
        self.moveCount = 0



    def getCoord(self):
        return self.coords

    #moves the bullet
    def moveSelf(self):
        self.coords = self.getNext()

    #draws the bullet
    def drawSelf(self):
        x = self.coords['x'] * CELLSIZE
        y = self.coords['y'] * CELLSIZE
        xcenter = self.coords['x'] * CELLSIZE + math.floor(CELLSIZE / 2)
        ycenter = self.coords['y'] * CELLSIZE + math.floor(CELLSIZE / 2)
        pygame.draw.circle(DISPLAYSURF, PINK, (xcenter, ycenter), RADIUS)

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

    def rotate(self,rotDir = 0):
        if rotDir == 0:
            rotDir = self.rotDir
        self.setDir((self.dirNum + rotDir) % 4)  # shift direction

    def hit(self, coord):
        return self.coords == coord

    def getDirNum(self):
        counter = 0
        found = False
        for dir in DIRECTIONS:
            if(not found):
                found = self.direction == dir
                if(not found):
                    counter = counter + 1
        return counter

    def setDir(self, num):
        self.direction = DIRECTIONS[num]
        self.dirNum = self.getDirNum()