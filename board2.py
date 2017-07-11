import pygame, os
from pygame.locals import *

from frequency2 import *

    
offset = 40
marge = 5 * offset

def loadImage(imageName):
    return pygame.image.load(os.path.join(imageName))

vierkant        = loadImage("vierkant.png")
vierkant2        = loadImage("vierkant2.png")
boardImage      = loadImage("Spelbord.png")

greybackground   = loadImage("greyimage2.jpg")
greyhover        = loadImage("greyhover.png")
buy              = loadImage("buy.png")
buyw             = loadImage("buyw.png")
nextturnw        = loadImage("nextturnw.png")
nextturn         = loadImage("next turn.png")
backtomenu       = loadImage("BackToMenu.png")
attack           = loadImage("attackbutton.png")
attackglow       = loadImage("attackglow.png")
backtomenuglow   = loadImage("BackToMenuGlow.png")
transparent   = loadImage("transparent.png")



UNIT_BUTTON_HOVER_IMAGE = pygame.transform.scale(greyhover, (int(offset), int(offset)))

width   = 1200
height  = 800

white   = (255,255,255)


MENU_POSITION = [ (0.94, 4.5), (24.5, 4.5), (0.94, 9.9), (24.5, 10) ]

LAND_TYPE = [ "Swamp", "Ice plains", "Desert",  "Forrest", "Goldmine" ]
SWAMP      = 0
ICE_PLAINS = 1
DESERT     = 2
FORREST    = 3
GOLDMINE   = 4
WATER      = 5
                      
BOARD_LAND_TYPE   = [ [ 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1 ],
                      [ 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1 ],
                      [ 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1 ],
                      [ 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1 ],
                      [ 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1 ],
                      [ 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1 ],
                      [ 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1 ],
                      [ 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5 ],
                      [ 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5 ],
                      [ 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5 ],
                      [ 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5 ],
                      [ 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3 ],
                      [ 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3 ],
                      [ 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3 ],
                      [ 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3 ],
                      [ 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3 ],
                      [ 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3 ],
                      [ 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3 ] ]
        
Slate_Gray      = (112,138,144)
Dim_Gray        = (96,96,96)

screen  = pygame.display.set_mode((width , height))


class Board:

    def __init__(self, game):
        self.game = game
        self.hover_list = [ [], [], [], [] ]

        self.drawBoard()
        self.buildMenu()
        pygame.display.flip()
        
    def update(self, event):
        for hover_item in self.hover_list[self.game.frequency.activePlayer]:
            hover_item.update(event)

        for squareList in self.boardSquares:
            for square in squareList:
                square.update(event)



    def placeText(self, x, y, text, size,  color):
        font     = pygame.font.SysFont("Bauhaus 93", size)
        position = (x * offset , y * offset)
        screen.blit(font.render(text, True, color), position)

    def displayMessage(self, message):
        x = 6.25
        y = 0.5
        color = self.game.frequency.getActivePlayer().colors[1]
        updateArea = pygame.Rect(x*offset, y*offset, 6*offset, offset/1.5)
        screen.blit(greybackground, updateArea.topleft, updateArea)
        self.placeText(x, y, message, 17, color)
        pygame.display.update(updateArea)

    def displayMessage2(self, message):
        x = 6.25
        y = 1.0
        color = self.game.frequency.getActivePlayer().colors[1]
        updateArea = pygame.Rect(x*offset, y*offset, 6*offset, offset/1.5 )
        screen.blit(greybackground, updateArea.topleft, updateArea)
        self.placeText(x, y, message, 17, color)
        pygame.display.update(updateArea)

    def displayWiningMessage3(self, message):
        x           = 8
        y           = 9
        color       = self.game.frequency.getActivePlayer().colors[1]
        updateArea  = pygame.Rect(x*offset, y*offset, 30*offset, offset*8 )

        screen.blit( transparent, updateArea.topleft, updateArea)
        self.placeText(x, y, message, 70, color)
        pygame.display.update(updateArea)



    def placeUnit(self, x,y,piece):
        updateArea      = pygame.Rect(x * offset + marge, y * offset + 30, offset, offset)
        positionBoard   = (x * offset + marge, y * offset + 30)
        areaBoard       = ((x-1) * offset, (y-1) * offset, offset, offset)
        screen.blit(pygame.transform.scale(boardImage, (offset * 18, offset * 18)), positionBoard, areaBoard)
        screen.blit(pygame.transform.scale( piece, updateArea.size ), updateArea.topleft)
        pygame.display.update(updateArea)

    def placeUnitButton(self, x, y, playerNumber, unit):
        position = (x * offset, y * offset)
        self.hover_list[playerNumber].append(UnitButton(self.game.unitSelectedAction, position, unit))

    def drawBoard(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption('frequency Game')
    
        screen.blit(greybackground,(0,0))
        screen.blit(pygame.transform.scale(boardImage, (offset * 18, offset * 18)), (offset + marge ,offset+30)) #descend the board with 20 pixels morde

        self.boardSquares = []

        for x in range(1, 19):
            self.boardSquares.append([])
            for y in range(1, 19):
                screen.blit(pygame.transform.scale( vierkant, (offset, offset)), (x * offset + marge ,y * offset+30 )) #descend the grids with 20 pixels morde
                self.boardSquares[x-1].append(BoardSquareButton(self.game.selectBoardSquareAction, self, x, y))

    def buildMenu(self):
        for i in range(2):
            self.buildPlayerMenu(i)

    def showMoney(self, playerNumber):
        position = MENU_POSITION[playerNumber]
        colors = self.game.COLOR_LIST[playerNumber]
        x = position[0] + 1.0
        y = position[1] + 7.6
        
        fontsizeMoney = 28

        updateArea = pygame.Rect(x*offset, y*offset, 4*offset, offset)
        screen.blit(greybackground, updateArea.topleft, updateArea)
        self.placeText( x, y,"f"+ str(self.game.frequency.player_list[playerNumber].money), fontsizeMoney, colors[0] )
        pygame.display.update(updateArea)
        
    def buildPlayerMenu(self, playerNumber):
        line_distance   = 1.2
        position        = MENU_POSITION[playerNumber]
        colors          = self.game.COLOR_LIST[playerNumber]

        x               = position[0]# x
        y               = position[1]# y
        
        # show money
        self.showMoney(playerNumber)

        # show buy / attack / next
        buttonSize = ( 63.999, 40 )
        button_y = ( y + line_distance * 7 )
        self.hover_list[playerNumber].append(ActionButton(self.game.buyAction, colors, buy, buyw, ((x - 0.1) * offset, button_y * offset), buttonSize))
        self.hover_list[playerNumber].append(ActionButton(self.game.attackAction, colors, attack, attackglow, ((x + 1.5) * offset, button_y * offset), buttonSize))
        self.hover_list[playerNumber].append(ActionButton(self.game.nextAction, colors, nextturn, nextturnw, ((x + 3.1) * offset, button_y * offset), buttonSize))

        # show unit prices
        if x > 15:
            x = x + 1
            
        fontsize36 = 36
        fontsize20 = 18    

        self.placeText(x, y, LAND_TYPE[playerNumber], fontsize36, colors[1])
        self.placeText(x, y + line_distance,   "Soldier  f" + str(self.game.UNIT_COSTS[playerNumber][0]), fontsize20,   colors[1])
        self.placeText(x, y + line_distance*2, "Robot    f" + str(self.game.UNIT_COSTS[playerNumber][1]),    fontsize20,   colors[1])
        self.placeText(x, y + line_distance*3, "Tank     f" + str(self.game.UNIT_COSTS[playerNumber][2]),     fontsize20,   colors[1])
        self.placeText(x, y + line_distance*4, "Barak    f" + str(self.game.UNIT_COSTS[playerNumber][3]),    fontsize20,   colors[1])
        self.placeText(x, y + line_distance*5, "Boat     f" + str(self.game.UNIT_COSTS[playerNumber][4]),    fontsize20,   colors[1])

        # show unit buttons
        if x < 15:
            x = x + 3.5
        else:
            x = x - 1.5
        y = y + 0.8
        
        player = self.game.frequency.player_list[playerNumber]
        self.placeUnitButton(x, y, playerNumber, player.soldier)
        self.placeUnitButton(x, y + line_distance, playerNumber, player.robot)
        self.placeUnitButton(x, y + line_distance*2, playerNumber, player.tank)
        self.placeUnitButton(x, y + line_distance*3, playerNumber, player.barrack)
        self.placeUnitButton(x, y + line_distance*4, playerNumber, player.boat)
     
     
class Button:
    def __init__(self, clickAction, image, hover_image, pos):
        self.hover          = False
        self.mouseDown      = False
        self.clickAction    = clickAction
        self.image          = image
        self.hover_image    = hover_image
        self.rect           = image.get_rect()
        self.rect.topleft   = pos
        self.noHoverAction()
        pygame.display.update(self.rect)

    def detectHover(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def update(self, event):
        if self.detectHover():
            if not(self.hover):
                self.hover = True
                self.hoverAction()
                pygame.display.update(self.rect)

            if not(self.mouseDown) and event.type == pygame.MOUSEBUTTONDOWN:
                # mouse button is pressed down, no action
                self.mouseDown = True
            elif self.mouseDown and event.type == pygame.MOUSEBUTTONUP:
                # mouse button is released, take action
                self.mouseDown = False
                self.clickAction(self)

        else:
            self.mouseDown = False
            if self.hover:
                self.hover = False
                self.noHoverAction()
                pygame.display.update(self.rect)


class BoardSquareButton(Button):
    def __init__(self, clickAction, board, x, y):
        self.board = board
        self.x = x
        self.y = y
        
        self.unit = None

        self.landType = BOARD_LAND_TYPE[y-1][x-1]
            
        pos = (x * offset + marge, y * offset+30 )
        Button.__init__(self, clickAction, vierkant, None, pos)
        
        self.rect = pygame.Rect(pos[0], pos[1], offset, offset)
        
    def isWater(self):
        return self.landType == WATER

    def isLand(self):
        return self.landType != WATER

    def isGoldMine(self):
        return self.landType == GOLDMINE

    def hasBarrack(self):
        return isinstance(self.unit, Barrack)

    def hasBoat(self):
        return isinstance(self.unit, Boat)

    def isEmpty(self):
        return self.unit == None

    def isEmptyBoat(self):
        return self.hasBoat() and self.unit.unitOnBoat == None

    def moveOntoBoat(self, unit):
        self.unit.unitOnBoat = unit
        self.board.placeUnit(self.x, self.y, unit.image)

    def removeUnitFromBoat(self):
        self.unit.unitOnBoat = None
        self.board.placeUnit(self.x, self.y, self.unit.image)

    def getPlayer(self):
        if self.unit == None:
            return None
        else:
            return self.unit.player

    def placeUnit(self, unit):
        self.unit = unit
        if isinstance(unit, Boat) and unit.unitOnBoat is not None:
            self.board.placeUnit(self.x, self.y, unit.unitOnBoat.image)
        else:
            self.board.placeUnit(self.x, self.y, unit.image)

    def removeUnit(self):
        self.unit = None
        self.board.placeUnit(self.x, self.y, vierkant)
    def removeUnit2(self):
        self.unit = None
        self.board.placeUnit(self.x, self.y, vierkant2)
    def distance(self, square):
        return max(abs(square.x - self.x), abs(square.y - self.y))

    def noHoverAction(self):
        return

    def hoverAction(self):
        return
#

class ActionButton(Button):
    def __init__(self, clickAction, colors, image, hover_image, pos, size):
        self.colors = colors
        self.rectangle = [ pos[0], pos[1], size[0], size[1] ]
        self.image_position = ( pos[0], pos[1] - 0.22 * offset )
        
        Button.__init__(self, clickAction, image, hover_image, pos)
        
        # groter rechthoek zodat je overal op de button kunt klikken en niet alleen op de tekst van het plaatje
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def blit(self, image, color):
        pygame.draw.rect(screen, color, self.rectangle)
        screen.blit(image, self.image_position )

    def noHoverAction(self):
        self.blit(self.image, self.colors[0])
        
    def hoverAction(self):
        self.blit(self.hover_image, self.colors[2])

    def reset(self):
        self.noHoverAction()
        pygame.display.update(self.rect)
        

def shiftPosition(pos, x, y):
    xy = list(pos)
    return (int(xy[0] + (x/2)), int(xy[1] + (y/2)))
    
    
class UnitButton(Button):
    def __init__(self, clickAction, pos, unit):
        self.unit = unit

        Button.__init__(self, clickAction, unit.image, UNIT_BUTTON_HOVER_IMAGE, pos)

        # kleiner rechthoek zodat het niet overlapt met andere unit buttons
        self.rectsmall = self.rect.inflate(int(-offset/2),int(-offset/2))
        self.rectsmall.topleft = shiftPosition(pos, offset/2, offset/2)
        
    def noHoverAction(self):
        screen.blit(greybackground, self.rect.topleft, self.rect)
        screen.blit(self.unit.image, self.rect.topleft)
        
    def hoverAction(self):
        screen.blit(self.hover_image, self.rectsmall.topleft)

