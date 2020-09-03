import pygame,block
from block import *
pygame.init()
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
BOXSIZE = 20
BOARDWIDTH = 30
BOARDHEIGHT = 32
SIDEMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5
BLANK = '.'
WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (155,0,0)
GREEN       = (0,155,0)
BLUE        = (0,0,155)
YELLOW      = (155,155,0)
KK          = (255, 255, 153)

TEXTCOLOR = BLACK
BGCOLOR = KK
COLORS = (BLUE,GREEN,RED,YELLOW)
try:
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
except:
    print "ok"
BORDERCOLOR = WHITE
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
BIG1 = pygame.font.Font('freesansbold.ttf',30)
TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

def convertToPixelCoords(boxx, boxy):
    # Convert the given xy coordinates of the board to xy
    # coordinates of the location on the screen.
    display=0
    return (SIDEMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))
def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
    scor=0
    if color == BLANK:
	scor+=10
        return
    if pixelx == None and pixely == None:
	scor+=10
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
	flag=False
    pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
def drawBoard(board):
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (SIDEMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, (SIDEMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
    # draw the individual boxes on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])
def drawStatus(score, level):
    # draw the score text
    scoreSurf = BIG1.render('Score: %s' % score, True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    # draw the level text
    levelSurf = BIG1.render('Level: %s' % level, True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150, 50)
    DISPLAYSURF.blit(levelSurf, levelRect)
def drawPiece(piece, pixelx=None, pixely=None):
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])
    # draw each of the boxes that make up the piece
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                display=1
                drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))
