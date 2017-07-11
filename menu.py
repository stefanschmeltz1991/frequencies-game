import pygame, os, sys, time, webbrowser
from pygame.locals import *
from game import *
from game2 import *





white = (255,255,255)
grey = (100,100,100)

pygame.init()
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
        if self.hovered == True:
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
            main()
            reset()

        if self.text == "2 players":
            screen          = pygame.display.set_mode((1200 , 800))
            main2()
            reset()
        if self.text == "GAME INSTRUCTIONS":
            webbrowser.open_new("file://" + os.path.realpath("Manual.pdf"))
        if self.text == "EXIT GAME":
            pygame.quit()
            quit()

        if self.text == "visit website":
            webbrowser.open_new("https://frequency262.wordpress.com")

#https://wordpress.com/post/frequency262.wordpress.com/5
menu_font = pygame.font.SysFont("Bauhaus 93", 50)

options = [Option("NEW GAME", (240, 200)),
           Option("GAME INSTRUCTIONS", (120, 250)),
           Option("EXIT GAME", (240, 300)),
           Option("visit website", (240, 350)),
           Option("2 players", (240, 400))]

def loadMusic():
    pygame.mixer.music.load('loopbgmusic.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.01)
def stopmusic():
        pygame.mixer.music.stop()




def reset():
    screen = pygame.display.set_mode((800, 600))
    screen.blit(bg,(1,1))
    screen.blit(logo,(10,-70))

def menu():
    reset()
    loadMusic()


    while True:

        pygame.event.pump()

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

menu()



