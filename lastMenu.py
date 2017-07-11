import pygame, os, sys, time
from pygame.locals import *
from lastgame import *


pygame.init()
screen = pygame.display.set_mode((800, 600))
white = (255,255,255)
grey = (100,100,100)
#background = pygame.image.load(os.path.join("Spelbordformenu.png"))
bg   = pygame.image.load(os.path.join("Spelbordmenu.png"))
logo = pygame.image.load(os.path.join("bg.png"))

class Option:
    hovered = False

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (white)
        else:
            return (grey)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def klickdown(self):
        if self.text == "NEW GAME":
            screen          = pygame.display.set_mode((1200 , 800))
            Main()
        if self.text == "GAME INSTRUCTIONS":
            pass
        if self.text == "EXIT GAME":
            pygame.quit()
            quit()

menu_font = pygame.font.SysFont("Bauhaus 93", 70)

options = [Option("NEW GAME", (220, 200)),
           Option("GAME INSTRUCTIONS", (90, 300)),
           Option("EXIT GAME", (220, 400))]

while True:
    pygame.event.pump()
    screen.blit(bg,(1,1))
    screen.blit(logo,(100,100))
    ev = pygame.event.get()
    for event in ev:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            if option.hovered:
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        option.klickdown()


            option.draw()
        pygame.display.flip()
