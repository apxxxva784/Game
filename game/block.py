import time
S_SHAPE= [['.....','.....','..OO.','.OO..','.....'],['.....','..O..','..OO.','...O.','.....']]
Z_SHAPE= [['.....','.....','.OO..','..OO.','.....'],['.....','..O..','.OO..','.O...','.....']]
I_SHAPE= [['..O..','..O..','..O..','..O..','.....'],['.....','.....','OOOO.','.....','.....']]
O_SHAPE= [['.....','.....','.OO..','.OO..','.....']]
J_SHAPE= [['.....','.O...','.OOO.','.....','.....'],['.....','..OO.','..O..','..O..','.....'],['.....','.....','.OOO.','...O.','.....'],['.....','..O..','..O..','.OO..','.....']]
T_SHAPE= [['.....','..O..','.OOO.','.....','.....'],['.....','..O..','..OO.','..O..','.....'], ['.....','.....','.OOO.','..O..','.....'],['.....','..O..','.OO..','..O..','.....']]
scor=0
PIECES = {'I': I_SHAPE,'O': O_SHAPE,'Z': Z_SHAPE,'S': S_SHAPE,'J': J_SHAPE,'T': T_SHAPE}
class block:
    def rotate(self,fallingPiece):
        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
    def move_left(self,fallingPiece):
        fallingPiece['x'] -= 1
        movingLeft = True
        movingRight = False
        lastMoveSidewaysTime = time.time()
    def move_right(self,fallingPiece):
        fallingPiece['x'] += 1
        movingRight = True
        movingLeft = False
        lastMoveSidewaysTime = time.time()
    def terms():
        pygame.quit()
        sys.exit()
