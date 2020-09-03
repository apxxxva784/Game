from board import board1
from board import TEMPLATEWIDTH
from board import TEMPLATEHEIGHT
from board import BOARDWIDTH
from board import BOARDHEIGHT
from board import BLANK
board=board1()
class TestBoard():
	def test_initialconditions1(self):
		assert TEMPLATEWIDTH == 5
	def test_initialconditions2(self):
		assert TEMPLATEHEIGHT == 5
	def test_initialconditions3(self):
		assert BOARDWIDTH == 30
	def test_initialconditions4(self):
		assert BOARDHEIGHT == 32
	def test_initialconditions7(self):
		assert BLANK == '.'

	



	
