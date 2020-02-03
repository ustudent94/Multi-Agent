from Assn2.Constant import *
import pygame, random

class Wall:

    def __init__(self):
        self.direction = UP
        self.coords = [{'x': 0, 'y': CELLHEIGHT}]
        self.initCoords()


    def getCoord(self):
        return self.coords

    def initCoords(self):
        #Bordering wall
        for direction in DIRECTIONS:
            self.direction = direction
            while not self.hitEdge():
                self.addWall()


    #draws the rocks
    def drawSelf(self):
        for coord in self.coords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            Rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(DISPLAYSURF, GREY, Rect)
            innerRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(DISPLAYSURF, WHITE, innerRect)

    def addWall(self):
        # move the wall by adding a segment in the direction it is moving
        if self.direction == UP:
            newBlock = {'x': self.coords[-1]['x'], 'y': self.coords[-1]['y'] - 1}
        elif self.direction == DOWN:
            newBlock = {'x': self.coords[-1]['x'], 'y': self.coords[-1]['y'] + 1}
        elif self.direction == LEFT:
            newBlock = {'x': self.coords[-1]['x'] - 1, 'y': self.coords[-1]['y']}
        elif self.direction == RIGHT:
            newBlock = {'x': self.coords[-1]['x'] + 1, 'y': self.coords[-1]['y']}
        #1 in 5 chance of jagged wall
        if random.randint(0, CELLWIDTH - 1) % 5 == 0:
            self.addJagged()
        self.coords.append(newBlock)  # have already removed the last segment
    def addJagged(self):
        if self.direction == UP:
            newBlock = {'x': self.coords[-1]['x'] + 1, 'y': self.coords[-1]['y']}
        elif self.direction == DOWN:
            newBlock = {'x': self.coords[-1]['x'] - 1, 'y': self.coords[-1]['y']}
        elif self.direction == LEFT:
            newBlock = {'x': self.coords[-1]['x'], 'y': self.coords[-1]['y'] - 1}
        elif self.direction == RIGHT:
            newBlock = {'x': self.coords[-1]['x'], 'y': self.coords[-1]['y'] + 1}
        if (not self.corner(newBlock)):
            self.coords.append(newBlock)  # have already removed the last segment

    def hitEdge(self):
        #return self.coords[-1]['x'] == -1 or self.coords[-1]['x'] == CELLWIDTH or self.coords[-1]['y'] ==-1 or self.coords[-1]['y'] == CELLHEIGHT
        hit = False
        if(self.direction == RIGHT and self.coords[-1]['x'] == CELLWIDTH -1):
            hit = True
        if (self.direction == DOWN and self.coords[-1]['y'] == CELLHEIGHT-1):
            hit = True
        if (self.direction == LEFT and self.coords[-1]['x'] == 0):
            hit = True
        if (self.direction == UP and self.coords[-1]['y'] == 0):
            hit = True
        return hit

    def hit(self, coord):
        hit = False
        for block in self.coords:
            if block == coord:
                hit = True
        return hit

    def corner(self,newBlock):
        corner = False
        #bottom left
        if(newBlock['x'] == 1 and newBlock['y'] == CELLHEIGHT-2):
            corner = True
        if(newBlock['x'] == 1 and newBlock['y'] == CELLHEIGHT-3):
            corner = True
        if(newBlock['x'] == 2 and newBlock['y'] == CELLHEIGHT-2):
            corner = True

        #bottom right
        if(newBlock['x'] == CELLWIDTH-2 and newBlock['y'] == CELLHEIGHT-2):
            corner = True
        if(newBlock['x'] == CELLWIDTH-2 and newBlock['y'] == CELLHEIGHT-3):
            corner = True
        if(newBlock['x'] == CELLWIDTH-3 and newBlock['y'] == CELLHEIGHT-2):
            corner = True

        #top right
        if(newBlock['x'] == CELLWIDTH-2 and newBlock['y'] == 1):
            corner = True
        if(newBlock['x'] == CELLWIDTH-2 and newBlock['y'] == 2):
            corner = True
        if(newBlock['x'] == CELLWIDTH-3 and newBlock['y'] == 1):
            corner = True

        #top left
        if(newBlock['x'] == 1 and newBlock['y'] == 1):
            corner = True
        if(newBlock['x'] == 1 and newBlock['y'] == 2):
            corner = True
        if(newBlock['x'] == 2 and newBlock['y'] == 1):
            corner = True

        return corner
