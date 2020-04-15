import pygame, sys
from pygame.locals import *

class rectObj:
    def __init__(self, color, rex):
        self.rowVal = 0#rowVal
        self.rowHeight = 0#rowHeight
        self.x = 0
        self.y = 0#co-ords for printing
        self.rec = rex
        self.color = color
    def getRex(self):
        return self.rec
    def setColor(self,color):
        self.color = color

rex_list = []    

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)
    ORANGE = (252, 155, 64)

    DISPLAY.fill(WHITE)

    ##  1,2 x,y location (3  length)  (4 height) 
    #pygame.draw.rect(DISPLAY,BLUE,(10,340,50,50))

    row = 1
    height = 1

    ## have to start storing those two values and then adding on thats why I cant see anything else
    rowVal = 10
    rowHeight = 340
    while (height != 4):
        rowVal = 10
        while (row < 5):
            #pygame.draw.rect(DISPLAY,BLUE,( 10*row + 10*row, 340 - (50*height)-(10*height),50,50))
            rex = pygame.Rect(rowVal, rowHeight,50,50)
            pygame.draw.rect(DISPLAY,BLUE, rex)
            rex_list.append(rectObj(BLUE,rex)) #conceptually big enough - cant store pygame.draw.rect 

            rowVal += 60

            print("1")
            row = row+1
            
        print("jj")
        row = 1 # obvious problem it was looping on the height but never got inside the inner loop after the first run
        height = height + 1
        rowHeight -= 60


   
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for rex in rex_list:
                    vv = rex.getRex()
                    if vv.collidepoint(pos):
                        print("C")
                        pygame.draw.rect(DISPLAY,ORANGE,rex.getRex())
                        rex.setColor(ORANGE)
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
