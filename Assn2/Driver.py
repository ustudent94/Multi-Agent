# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import pygame, sys
from pygame.locals import *

from Assn2.Constant import *




assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."




def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Roomba')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    from Assn2.Wall import Wall
    from Assn2.Roomba import Roomba
    from Assn2.Dirt import Dirt
    from Assn2.Obstacle import Obstacle
    from Assn2.MovingObstacle import MovingObstacle
    numDirt = 100
    count = 0
    detached = False
    rotated = False
    blindMove = False

    wall = Wall()
    roombas = [Roomba(1,UP,BLUE),Roomba(2,DOWN,GREEN,{'x': CELLWIDTH -2, 'y': 1},-1,-1)]
    dirt=[]
    obstacles = [Obstacle(3,RIGHT,5,37,'furniture'),Obstacle(3,LEFT,CELLWIDTH-5,10,'drop'),Obstacle(3,UP,20,20,'generic'),Obstacle(3,DOWN,30,5,'table')]
    movingObstacle = MovingObstacle(LEFT,{'x': CELLWIDTH -2, 'y': 3})


    while count < numDirt:
        dirt.append(Dirt())
        while(wall.hit(dirt[count].getCoord())):
            dirt[count].newLocation()
        count = count +1

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                key = event.key
                if event.key == K_ESCAPE:
                    terminate()

        #control loop for each roomba
        for roomba in roombas:
            #suck up dirt if hit
            for pile in dirt:
                if(pile.hit(roomba.getCoord())):
                    pile.suckDirt()
                    roomba.maxDirt = max(roomba.maxDirt,pile.amount)


            #moving obstacle turn away if wall is hit
            while(wall.hit(movingObstacle.getNext())):
                movingObstacle.rotate(-1)

            for obstacle in obstacles:
                while(obstacle.hit(movingObstacle.getNext())):
                    movingObstacle.rotate(-1)

            if (movingObstacle.hit(roomba.getNext()) and (wall.hit(roomba.getNext(-1)) or roomba.finishedExteriorLoop )):
                obs = movingObstacle
                roomba.setAvoid()

            for obstacle in obstacles:
                if(obstacle.hit(roomba.getNext())):
                    obs = obstacle
                    roomba.setAvoid()

            if(roomba.avoid and roomba.returnToPath(obs)):
                roomba.rotate(1)
                roomba.avoid = False
            elif(roomba.avoid):
                while (obs.hit(roomba.getNext())):
                    roomba.rotate(1)
                if (not obs.hit(roomba.getNext(-1))):
                    roomba.rotate(-1)
            else:
                if(not roomba.finishedExteriorLoop):
                    while(wall.hit(roomba.getNext())):
                         roomba.rotate(1)
                    if(not wall.hit(roomba.getNext(-1)) and not roomba.seekPoint):
                        roomba.rotate(-1)

                if(roomba.finishedExteriorLoop and roomba.hitEdge() and not roomba.seekPoint):
                    roomba.rotate(1)
                    for obstacle in obstacles:
                        if (obstacle.hit(roomba.getNext())):
                            obs = obstacle
                            roomba.setAvoid()
                            roomba.rotate(1)

                if(roomba.seekPoint):
                    roomba.setHeading()

            #move objects
            roomba.moveSelf()

        if(movingObstacle.moveCount % 30 == 0):
            movingObstacle.moveSelf()
        movingObstacle.moveCount = movingObstacle.moveCount +1

        #roomba.hitEdge()
        #if (wall.hit(roomba.getNext())):
            #roomba.setWAC()
            #roomba.changeDirection()

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        wall.drawSelf()

        movingObstacle.drawSelf()
        for pile in dirt:
            pile.drawSelf()
        for obstacle in obstacles:
            obstacle.drawSelf()
        for roomba in roombas:
            roomba.drawSelf()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        #set something to end the loop
        #return

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, YELLOW)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Agent', True, GOLD, BLUE)
    titleSurf2 = titleFont.render('Roomba', True, WHITE)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (math.floor(WINDOWWIDTH / 2), math.floor(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (math.floor(WINDOWWIDTH / 2), math.floor(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    sys.exit()


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (math.floor(WINDOWWIDTH / 2), 10)
    overRect.midtop = (math.floor(WINDOWWIDTH / 2), gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()
