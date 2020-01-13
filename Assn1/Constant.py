import math

FPS = 3
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
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
YELLOW = (255,255,0)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntactic sugar: index of the worm's head
RADIUS = math.floor(CELLSIZE/2.5)