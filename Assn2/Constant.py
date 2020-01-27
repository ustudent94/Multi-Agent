import math,pygame

FPS = 250
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

CELLSIZE = 10

CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
BLUE      = (  0,   0, 255)
GOLD      = (255, 215,   0)
PINK      = (255, 105, 180)
RED       = (255,   0,   0)
GREY      = (169, 169, 169)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
YELLOW = (255,255,0)
BGCOLOR = BLACK
DARKBROWN = (139,  69,  19)
MIDBROWN  = (205, 133,  63)
LIGHTBROWN= (222, 184, 135)



UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntactic sugar: index of the worm's head
RADIUS = math.floor(CELLSIZE/2.5)
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
DIRECTIONS = [UP,RIGHT,DOWN,LEFT] #ORDER MATTERS