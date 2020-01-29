from Assn2.Constant import *
import pygame

class MovingObstacle:
    def __init__(self, direction,coords):
        self.direction = direction
        self.coords = [coords]

        #shifts bullet in front of head
        self.moveBullet()



    def getCoord(self):
        return self.coords

    #moves the bullet
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
        del self.coords[-1]

    #draws the bullet
    def drawSelf(self,DISPLAYSURF):
        x = self.coords[HEAD]['x'] * CELLSIZE
        y = self.coords[HEAD]['y'] * CELLSIZE
        xcenter = self.coords[HEAD]['x'] * CELLSIZE + math.floor(CELLSIZE / 2)
        ycenter = self.coords[HEAD]['y'] * CELLSIZE + math.floor(CELLSIZE / 2)
        pygame.draw.circle(DISPLAYSURF, PINK, (xcenter, ycenter), RADIUS)
