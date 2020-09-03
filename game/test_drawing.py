from drawing import WINDOWWIDTH ,WINDOWHEIGHT ,BOXSIZE ,BOARDWIDTH ,BOARDHEIGHT ,SIDEMARGIN ,TOPMARGIN ,BLANK ,WHITE,BLACK,RED,BLUE,YELLOW,KK,TEXTCOLOR, BGCOLOR ,COLORS ,BORDERCOLOR ,TEMPLATEWIDTH ,TEMPLATEHEIGHT
def test1():
	assert WINDOWWIDTH == 1000
def test2():
	assert WINDOWHEIGHT == 600
def test3():	
	assert BOXSIZE == 20
	
def test4():
	assert BOARDWIDTH == 30
def test5():
	assert BOARDHEIGHT == 32
def test6():
	assert 	SIDEMARGIN == int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
def test7():
	assert TOPMARGIN == WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5
def test8():
	assert BLANK == '.'
def test9():
	assert WHITE       == (255, 255, 255)
def test10():
	assert BLACK       == (  0,   0,   0)
def test11():
	assert RED         == (155,0,0)
def test13():
	assert BLUE        == (0,0,155)
def test14():
	assert YELLOW      == (155,155,0)
def test15():
	assert KK          == (255, 255, 153)

def test16():

	assert TEXTCOLOR == BLACK
def test17():
	assert BGCOLOR ==KK

def test19():
	

	assert BORDERCOLOR == WHITE
def test111():
	assert TEMPLATEWIDTH == 5
def test112():
	assert TEMPLATEHEIGHT == 5

 

