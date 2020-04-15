import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

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
            pygame.draw.rect(DISPLAY,BLUE,( rowVal, rowHeight,50,50))

            rowVal += 60

            print("1")
            row = row+1
            
        print("jj")
        row = 1 # obvious problem it was looping on the height but never got inside the inner loop after the first run
        height = height + 1
        rowHeight -= 60


    #row1 = 1
    #height1 = 1
    #while(height1 < 4):
       # while(row1 < 4):
       #     print("row")
      #  print("height")
       
            
    #pygame.draw.rect(DISPLAY,BLUE,(10,390,50,50)) //400 y co-ord is on the line - the drawing shape is top left corner down and across

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
