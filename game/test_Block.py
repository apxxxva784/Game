from block import block
from block import S_SHAPE
from block import Z_SHAPE
from block import I_SHAPE
from block import O_SHAPE
from block import J_SHAPE
from block import T_SHAPE
blocks=block()
class TestBlocks():
	def test_initial_S_SHAPE_TEMPLATE(self):
		assert S_SHAPE == [['.....',
	                     '.....',
	                     '..OO.',
	                     '.OO..',
	                     '.....'],
	                    ['.....',
	                     '..O..',
	                     '..OO.',
	                     '...O.',
	                     '.....']]
 	def test_initial_Z_SHAPE_TEMPLATE(self):
		assert Z_SHAPE == [['.....',
		                     '.....',
		                     '.OO..',
		                     '..OO.',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '.OO..',
		                     '.O...',
		                     '.....']]
 	def test_initial_I_SHAPE_TEMPLATE(self):
		assert I_SHAPE == [['..O..',
		                     '..O..',
		                     '..O..',
		                     '..O..',
		                     '.....'],
		                    ['.....',
		                     '.....',
		                     'OOOO.',
		                     '.....',
		                     '.....']]
 	def test_initial_O_SHAPE_TEMPLATE(self):
		assert O_SHAPE == [['.....',
		                     '.....',
		                     '.OO..',
		                     '.OO..',
		                     '.....']]
 	def test_initial_J_SHAPE_TEMPLATE(self):
		assert J_SHAPE == [['.....',
		                     '.O...',
		                     '.OOO.',
		                     '.....',
		                     '.....'],
		                    ['.....',
		                     '..OO.',
		                     '..O..',
		                     '..O..',
		                     '.....'],
		                    ['.....',
		                     '.....',
		                     '.OOO.',
		                     '...O.',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '..O..',
		                     '.OO..',
		                     '.....']]
 	def test_initial_T_SHAPE_TEMPLATE(self):
		assert T_SHAPE == [['.....',
		                     '..O..',
		                     '.OOO.',
		                     '.....',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '..OO.',
		                     '..O..',
		                     '.....'],
		                    ['.....',
		                     '.....',
		                     '.OOO.',
		                     '..O..',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '.OO..',
		                     '..O..',
		                     '.....']]
	def test_PIECES(self):
		blocks.PIECES = {'S': S_SHAPE,
      'Z': Z_SHAPE,
      'J': J_SHAPE,
      'I': I_SHAPE,
      'O': O_SHAPE,
      'T': T_SHAPE}	


	def test_move_left(self):
		fallingPiece={'x':0,'y':2,'rotation':2,'shape':'Z'
			}
		initialx=fallingPiece['x']
		blocks.move_left(fallingPiece)
		finalx=fallingPiece['x']
		assert finalx==initialx-1
	def test_move_right(self):
		fallingPiece={'x':0,'y':2,'rotation':2,'shape':'Z'
			}
		initialx=fallingPiece['x']
		blocks.move_right(fallingPiece)
		finalx=fallingPiece['x']
		assert finalx==initialx+1
	def test_rotate(self):
		fallingPiece={'x':0,'y':2,'rotation':2,'shape':'Z'
			}
		initialrotation=fallingPiece['rotation']
		blocks.rotate(fallingPiece);
		finalrotation=fallingPiece['rotation']
		assert finalrotation==(initialrotation+1)%2




			
	                     
	


