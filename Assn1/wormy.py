# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import pygame, sys
from pygame.locals import *

from Assn1.Constant import *




assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."




def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    from Assn1.Worm import Worm
    from Assn1.Apple import Apple
    from Assn1.Bullet import Bullet

    #Create array of worms
    worms = {Worm(1, K_UP, K_DOWN, K_RIGHT, K_LEFT,K_KP0, GREEN, RIGHT), Worm(2, K_w, K_s, K_d, K_a,K_SPACE, BLUE, RIGHT)}
    #for laptop debug
    #worms = {Worm(1, K_i, K_k, K_l, K_j, K_8, GREEN, RIGHT),Worm(2, K_w, K_s, K_d, K_a, K_2, BLUE, RIGHT)}


    # Start the apple in a random place.
    apples = {Apple(1),Apple(2)}

    #Start a list of bullets
    bullets = []

    #start a list of rocks
    rocks = []

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                key = event.key
                if event.key == K_ESCAPE:
                    terminate()
                else:
                    for worm in worms:
                        keyPressed = worm.containsKey(key)
                        if keyPressed:
                            worm.eventHandler(event)
                            #worm.moveWorm()
                            if worm.getFired():
                                bullets.append(worm.getBullet())



        # check if the worm has hit itself or the edge
        for worm in worms:
            hit = worm.hitSelf()
            if not hit:
                hit = worm.hitEdge()
                if not hit:
                    for bullet in bullets:
                        # check if head hit by bullet
                        hit = worm.hitObject(bullet.getCoord())
                        if not hit:
                            #checks for hits on body and turns tail to stone
                            tempRock = worm.tailToStone(bullet.getCoord()[0])
                            if not tempRock.isEmpty():
                                rocks.append(tempRock)
                        else:
                            return #game over
                    if not hit:
                        #check if hit rock
                        for rock in rocks:
                            if worm.hitObject(rock.getCoord()):
                                return #game over
            for otherWorm in worms:
                if otherWorm != worm and not hit:
                    hit = worm.hitObject(otherWorm.getCoord())

            #if worm hits game over
            if hit:
                return  # game over



            eaten = False
            #check to see if apple was eaten
            for apple in apples:
                eaten = worm.ateApple(apple.getCoord())
                if eaten:
                    apple.newLocation()
                    worm.addTail()

            # move the worm
            worm.moveWorm()
            worm.removeTail()

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        for worm in worms:
            worm.drawWorm(DISPLAYSURF)
            worm.drawScore(BASICFONT,DISPLAYSURF)
            #drawScore(worm.getScore(), worm.getId(), (worm.getId()-1)*120, 10)

        for apple in apples:
            apple.drawApple(DISPLAYSURF)

        for bullet in bullets:
            bullet.moveBullet()
            bullet.drawBullet(DISPLAYSURF)

        for rock in rocks:
            rock.drawRock(DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

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
    titleSurf1 = titleFont.render('Snake', True, GOLD, BLUE)
    titleSurf2 = titleFont.render('Game', True, WHITE)

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