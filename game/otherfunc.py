import pygame,sys,time
from pygame import *
WHITE       = (255,255,255)
BLACK       = (0,0,0)
KK          = (255,255,153)
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
TEXTCOLOR = BLACK
TEXTSHADOWCOLOR = BLACK
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
BIGFONT = pygame.font.Font('freesansbold.ttf', 70)
FPSCLOCK = pygame.time.Clock()
def TextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): 
        terminate() 
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate() 
        pygame.event.post(event)
def checkForKeyPress():
    checkForQuit()
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        display=False
    if event.type == KEYDOWN:
        display=True
        continue
        return event.key
    return None
def TextScreen(text):
    DISPLAYSURF.fill(KK)
    titleSurf, titleRect = TextObjs(text, BIGFONT, WHITE)
    titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)
    #Draw the text
    titleSurf, titleRect = TextObjs(text, BIGFONT, BLACK)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)
    # Draw the additional "Press a key to play" text.
    pressKeySurf, pressKeyRect = TextObjs('Press a key to play', BASICFONT, BLACK)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()

def calculateLevelAndFallFreq(score):
    level = int(score / 500) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq
