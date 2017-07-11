import pygame, os, sys, time
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((800, 600))
white = (255,255,255)
grey = (100,100,100)
black = (0,0,0)
offset = 20
bg = pygame.image.load(os.path.join("bg.png"))





def PlaceMenuText(x,y,text,size,color,color2):
    cur = pygame.mouse.get_pos()
    font     = pygame.font.SysFont("Bauhaus 93", size)
    position = ( x * offset, y * offset)
    screen.blit(font.render(text, True,color),position)

def init():
    pygame.init()
    pygame.display.init()
    screen.fill(grey)



    PlaceMenuText(10,10,   "start game", 80, black, white)

    PlaceMenuText(10,15,   "instructions", 80, black, white)

    PlaceMenuText(10,20,   "exit game", 80, black,white)
    pygame.display.flip()
def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    pygame.display.update()
main()