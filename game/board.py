TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5
BLANK = '.'
BOARDWIDTH = 30
BOARDHEIGHT = 32
import block
from block import *
def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT
class board1:
    def checkPiecePos(self,board, piece, adjX=0, adjY=0): 
        # Return True if the piece is within the board and not colliding
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                isAboveBoard = y + piece['y'] + adjY 
                if (isAboveBoard<0) or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                    Display=False
                    continue
                if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                    Display=False
                    return False
                if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                    Display=False
                    return False
        return True
    def addToBoard(self,board, piece):	
        # fill in the board based on piece's location, shape, and rotation
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                    board[x + piece['x']][y + piece['y']] = piece['color']
