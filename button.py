import pygame
#from game import  *

def shiftPosition(pos, x, y):
    xy = list(pos)
    return (int(xy[0] + (x/2)), int(xy[1] + (y/3))) # positie van doorzichtige vierkant

##############################################################

class Button:
    def __init__(self, clickAction, image, hover_image, pos):
        self.hover          = False
        self.click          = False
        self.clickAction    = clickAction
        self.image          = image
        self.hover_image    = hover_image
        self.rect           = image.get_rect()
        self.rect.topleft   = pos
        self.noHoverAction()
        pygame.display.update(self.rect)



    def Update(self):
        if self.detectHover():
            if not(self.hover):
                self.hover = True
                self.hoverAction()
                pygame.display.update(self.rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not(self.click):
                    self.click = True
                    self.clickAction(self)
            else:
                self.click = False
        else:
            self.click = False
            if self.hover:
                self.hover = False
                self.noHoverAction()
                pygame.display.update(self.rect)

    def detectHover(self):

        return self.rect.collidepoint(pygame.mouse.get_pos())