import random
import sys
import block
import board
import otherfunc
import drawing
from pygame.locals import *
from block import *
from board import *
from otherfunc import *
from drawing import *
import time
FPS = 25
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
BOXSIZE = 20
BOXLENTH = 100
BOARDWIDTH = 30
BOARDDEPTH = 10
BOARDHEIGHT = 32
BLANK = '.'

MOVESIDEWAYSFREQ = 0.15
SPACEFREQUENCY = 0.3
MOVEDOWNFREQ = 0.1

SIDEMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

#               R    G    B
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
Navy = (156,  156, 253)
GREEN = (0, 155,   0)
BLUE = (0,   0, 155)
YELLOW = (155, 155,   0)
KK = (255, 255, 153)

BORDERCOLOR = WHITE
BGCOLOR = KK
TEXTCOLOR = BLACK
TEXTFONTSIZE = 18
TEXTSHADOWCOLOR = WHITE
COLORS = (BLUE, GREEN, RED, YELLOW)

max_possible_blocks = 32*30*20

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5


class gameplay(block, board1):
    def getBlankBoard(self):
        # create and return a new blank board data structure
        board = []
        for i in range(BOARDWIDTH):
            board.append([BLANK] * BOARDHEIGHT)
        return board

    def checkRowEmpty(self, board, y):
        # Return True if the line filled with boxes with no gaps.
        for x in range(BOARDWIDTH):
            if board[x][y] == BLANK:
                return False
        return True

    def selectPiece(self):
        # return a random new piece in a random rotation and color
        shape = random.choice(list(PIECES.keys()))
        newPiece = {'shape': shape, 'rotation': random.randint(0, len(PIECES[shape]) - 1), 'x': int(
            BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2), 'y': -2, 'color': random.randint(0, len(COLORS)-1)}
        scor = 100
        display = 1
        return newPiece

    def updatescore(self, score, board):
        score += 10
        score += (100*removeCompleteLines(board))
        return score


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT, bg
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 70)
    BIG1 = pygame.font.Font('freesansbold.ttf', 30)
    pygame.display.set_caption('Tetris')
    TextScreen('Tetris')
    # screen=pygame.display.set_mode(size)
    bg = pygame.image.load("water.jpg")
    bg = pygame.transform.scale(bg, (1000, 600))
    while True:  # game loop
        # screen.blit(bg,(0,0))
        runGame()
        TextScreen('Game Over')


def runGame():
    size = [1000, 600]
    screen = pygame.display.set_mode(size)
    # setup variables for the start of the game
    game = gameplay()
    bo = board1()
    blo = block()
    board = game.getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingLeft = False
    movingRight = False
    movingDown = False
    score = 0
    level, fallFreq = calculateLevelAndFallFreq(score)
    fallingPiece = game.selectPiece()
    nextPiece = game.selectPiece()
    while True:  # game loop
        if fallingPiece == None:
            # No falling piece in play, so start a new piece at the top
            fallingPiece = nextPiece
            nextPiece = game.selectPiece()
            lastFallTime = time.time()  # reset lastFallTime
            if not bo.checkPiecePos(board, fallingPiece):
                display_score = 1  # Flag for score
                return  # can't fit a new piece on the board, so game over
        checkForQuit()
        for event in pygame.event.get():  # event handling loop
            if event.type == KEYUP:
                if (event.key == K_a):
                    movingLeft = False
                elif (event.key == K_d):
                    movingRight = False
                elif (event.key == K_SPACE):
                    movingDown = False
                scor = 0
            elif event.type == KEYDOWN:
                # moving the piece left
                if (event.key == K_a) and bo.checkPiecePos(board, fallingPiece, adjX=-1):
                    blo.move_left(fallingPiece)
                # moving piece to right
                elif (event.key == K_d) and bo.checkPiecePos(board, fallingPiece, adjX=1):
                    blo.move_right(fallingPiece)
                # rotating the piece (if there is room to rotate)
                elif (event.key == K_s):
                    blo.rotate(fallingPiece)
                # move the current piece all the way down
                elif (event.key == K_SPACE):
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not bo.checkPiecePos(board, fallingPiece, adjY=i):
                            break
                    fallingPiece['y'] += (i-1)
        # handle moving the piece because of user input
        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and bo.checkPiecePos(board, fallingPiece, adjX=-1):
                fallingPiece['x'] -= 1
            elif movingRight and bo.checkPiecePos(board, fallingPiece, adjX=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()
        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and bo.checkPiecePos(board, fallingPiece, adjY=1):
            Display = False
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()
        # let the piece fall if it is time to fall
        if time.time() - lastFallTime > fallFreq:
            # see if the piece has landed
            if not bo.checkPiecePos(board, fallingPiece, adjY=1):
                # falling piece has landed, set it on the board
                bo.addToBoard(board, fallingPiece)
                score = game.updatescore(score, board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None
            else:
                # piece did not land, just move the piece down
                fallingPiece['y'] += 1
                lastFallTime = time.time()
        # drawing everything on the screen
        DISPLAYSURF.fill(BGCOLOR)
        screen.blit(bg, (0, 0))
        drawBoard(board)
        drawStatus(score, level)
        if fallingPiece != None:
            drawPiece(fallingPiece)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def removeCompleteLines(board):
    num = 0
    y = BOARDHEIGHT-1  # start y at the bottom of the board
    game1 = gameplay()
    while y >= 0:
        if game1.checkRowEmpty(board, y):
            # Remove the line and pull boxes down by one line.
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            num += 1
        else:
            y -= 1  # move on to check next row up
    return num


if __name__ == '__main__':
    main()
