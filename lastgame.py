import pygame, os,sys
from pygame.locals import *
from playerx import *
########################################################################

RED             = [ (102,0,0),      (178,34,34),     (128,0,0) ]
GREEN           = [ (0,51,0),       (0,100,0),       (0,128, 0) ]
BLUE            = [ (0,0,128),      (65,105,225),    (0,0,205) ]
YELLOW          = [ (218,165,32),   (255,215,0 ),    (240,230,140) ]

#########################################################################

COLOR_LIST      = [ RED,   BLUE ,  YELLOW,    GREEN ]
COLOR_NAMES     = [     "red",    "blue",     "yellow",      "green"  ]
LAND_TYPE       = [       "Swamp",     "Ice plains",     "Desert",   "Forest"  ]
MENU_POSITION   = [   (1, 0),     (24.5, 0),  (1, 10),    (24.5, 10) ]
UNIT_COST       = [[150, 300, 750, 500, 800 ],\
                   [120, 300, 750, 500, 1000],\
                   [150, 300, 600, 500, 1000],
                   [150,300,600,500,100]]
########################################################################
width           = 1200
height          = 800
vierkant        = pygame.image.load(os.path.join("vierkant.png"))
board           = pygame.image.load(os.path.join("Spelbord.png"))
white           = (255,255,255)
screen          = pygame.display.set_mode((width , height))

########################################################################

offset          = 40
marge           = 5 * offset

#######################################################################
greybackground   = pygame.image.load(os.path.join("greyimage.jpg"))
greyhover        = pygame.image.load(os.path.join("greyhover.png")).convert_alpha()
buy              = pygame.image.load(os.path.join("buy.png"))
buyw             = pygame.image.load(os.path.join("buyw.png"))
nextturnw        = pygame.image.load(os.path.join("nextturnw.png"))
nextturn         = pygame.image.load(os.path.join("next turn.png"))
backtomenu       = pygame.image.load(os.path.join("BackToMenu.png"))
attack           = pygame.image.load(os.path.join("attackbutton.png"))
attackglow       = pygame.image.load(os.path.join("attackglow.png"))
backtomenuglow   = pygame.image.load(os.path.join("BackToMenuGlow.png"))
#######################################################################
untibuttonhover = pygame.transform.scale(greyhover, (int(offset), int(offset))) # /2  /2

def shiftPosition(pos, x, y):
    xy = list(pos)
    return (int(xy[0] + (x/2)), int(xy[1] + (y/2)))  #(x/2)  (y/2)

class Hover:
    def __init__(self,clickAction, image, pos):
        self.Hover =False
        self.click =False
        self.clikAction = clickAction
        self.image = image
        self.hover_image = untibuttonhover
        self.rect = image.get_rect()
        self.rectsmall = self.rect.inflate(int(-offset/2),int(-offset/2))  #int(-offset/3),int(-offset/3)
        self.rect.topleft = pos
        self.rectsmall.topleft = shiftPosition(pos, offset/2, offset/2)

        self.nohoverAction()
        pygame.display.update(self.rect)

    def nohoverAction(self):
        screen.blit(self.image, self.colors[2])
    def hoverAction(self):


    def Update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not(self.Hover):
                self.Hover = True
                self.blit(self.hover_image, self.colors[2])
                pygame.display.update(self.rect)
             if event.type == pygame.MOUSEBUTTONDOWN:
                 if not (self.click):
                     self.click = True
                     self.clickAction()
             else:
                 self.click = False
        else:
            if (self.Hover):
                screen.blit(greybackground, self.rect.topleft, self.rect)
                screen.blit(self.image, self.rect.topleft)
                pygame.display.update(self.rect)
def placeUnit(button):
    print("placing unit")

class boardsquare(button):
    def __init__(self):
        pos = ( x * offset, y * offset)
        Button.__init__(self, placeUnit, vierkant, None, pos)

    def buyAction(button):
        print("buying unit")
    def attackAction(button):
        print ("attacking")
    def nextAction(button):
        global activePlayer, selectedUnit
        selectedUnit = None
        activePlayer = (activePlayer + 1) % 4 # wat er over blijft
        button.hover = False
        button.nohoverAction()
def noAction():
    print("no action")
def unitselectedAction(button):
    global selectedUnit
    selectedUnit = button.unit
    unit =  button.unit
    price = player_list[activePlayer][unit.name]
    print("selected unit" + unit.name + "price f " + str(price))




class ActionButton:
    def __init__(self, colors, image, hover_image, pos, size):
    #def __init__(self, colors, image, hover_image, pos, size):
        self.Hover          =False
        self.clickAction    =clickAction
        self.colors         = colors
        self.image          = image
        self.hover_image    = hover_image
        self.image_rect     = image.get_rect()
        self.rectangle      = [ pos[0], pos[1], size[0], size[1] ]
        self.image_position = ( pos[0], pos[1] - 0.22 * offset )   # - 0.22
        self.rect           = pygame.Rect(pos[0], pos[1], size[0], size[1])



    def blit(self,image, color):
        pygame.draw.rect(screen, colors, self.rectangle)
        screen.blit(image, image_position )
        pygame.display.update(self.rect)


    def Update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not(self.Hover):
                self.Hover = True
                self.blit(self.hover_image, self.colors[2])
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #clickAction()
        else:
            if (self.Hover):
                self.Hover = False
                self.blit(self.hover_image, self.colors[0])

#_____________HOVER OVER UNITS______________________________________________________________________#



#####################################BOARD & BACKGROUND#################################################################
def drawGUI():
    cur = pygame.mouse.get_pos()
    screen.blit(greybackground,(1,1))
    screen.blit(pygame.transform.scale(     board,       (offset * 18, offset * 18)),       (offset + marge ,offset+30)) #descend the board with 20 pixels morde

    for x in range(1, 19):
        for y in range(1, 19):
            if cur == True and   cur >1 and cur <19:
                screen.blit(pygame.transform.scale(     vierkant,      (offset, offset)),      (x * offset + marge ,y * offset+30 )) #descend the grids with 20 pixels morde


##################################PLACE PIECES(BAR)#####################################################################
def placepiece(x,y,piece):
    screen.blit(pygame.transform.scale(     piece,       (offset, offset)),      (x * offset + marge ,y * offset + 30 )) #descend the pieces  with 20 pixels morde

def placeBaracks():
    placepiece(1,1,greenbarrack)
    placepiece(1,18,redbarrack)
    placepiece(18,1,bluebarrack)
    placepiece(18,18,yellowbarrack)


#####################################TO DRAW THE UNITS ON THE BOARD#####################################################
def DrawUnits(self, screen, offset):
    POS_X = unit.x
    POS_Y = unit.y
    screen.blit(pygame.transform.scale(self.Texture, (offset, offset)),
                     (offset + self.Tile.Position.X * offset,
                      offset + self.Tile.Position.Y * offset))

def loadImages():
    global barracks, soldiers, boats, tanks, robots, harbors
    barracks = []
    soldiers = []
    boats    = []
    tanks    = []
    robots   = []
    harbors  = []
    for color in COLOR_NAMES:
        barracks.append(pygame.image.load(os.path.join(color + "bar.png")))
        soldiers.append(pygame.image.load(os.path.join(color + "soldier.png")))
        boats.append(pygame.image.load(os.path.join(   color + "boat.png")))
        tanks.append(pygame.image.load(os.path.join(   color + "tank.png")))
        robots.append(pygame.image.load(os.path.join(  color + "robot.png")))
        harbors.append(pygame.image.load(os.path.join( color + "harbor.png")))


###################################  PLACE TEXT & AND UNITS(BUY)  ######################################################
def placeText(x, y, text, size,  color):                   #
    font     = pygame.font.SysFont("Bauhaus 93", size)     #
    position = (x * offset , y * offset)                   #
    screen.blit(font.render(text, True, color),position)   #
############################################################
def unitsNotOnBoard(x, y, image, playernumber, unit):            #
    position = (x * 40, y * 40)
    unit = player_list[playernumber]
    hover_list[playernumber].append(Hover(image, position,unit))#
############################################################
#show money():





#show unit price






def buildMenu(playernumber):                    #4 players
    line_distance = 1.2
        
    position    = MENU_POSITION[playernumber]   #MENU_POSITION = [ (1, 0), (24.5, 0), (1, 10), (24.5, 10) ] the position of each menu.
    colors      = COLOR_LIST[playernumber]      #COLOR_LIST      = [ GREEN,   BLUE ,  RED,    YELLOW ]
    x           = position[0]
    y           = position[1]
    fontsizeMoney = 15
    #show buy
    fontsizeMoney = 28
    placeText(x+2,7.6, str(player_list[playernumber].money),fontsizeMoney,color[0])

    # / attack / next
    buttonSize = ( 60, 40 )
    button_y = ( y + line_distance * 7.3 ) * offset    #line distance for every square on the board
    placeText( x + 2 , y + 7.7, str(player_list[playernumber].Money), fontsizeMoney, colors[2])

    hover_list[playernumber].append(Button(colors, buy,      buyw,       ((x - 0.1) * offset,  button_y),  buttonSize)) #(self, colors, image, hover_image, pos, size):
    hover_list[playernumber].append(Button(colors, attack,   attackglow, ((x + 1.5) * offset,  button_y),  buttonSize)) #(self, colors, image, hover_image, pos, size):
    hover_list[playernumber].append(Button(colors, nextturn, nextturnw,  ((x + 3.1) * offset,  button_y),  buttonSize)) #(self, colors, image, hover_image, pos, size):

    if x > 15:
        x = x + 1
        
    fontsize36 = 36
    fontsize20 = 18

                                                                                  #mLAND_TYPE = [ "Forest","Ice plains","Desert","Swamp"]
    placeText(x, y,          LAND_TYPE[playernumber],    fontsize36,   colors[1]) #  placeText(x, y, text, size,  color)
    placeText(x, y + line_distance,   "Soldier  f ",+  str(UNIT_COSTS[playernumber][0]), fontsize20,   colors[1])
    placeText(x, y + line_distance*2, "Tank     f",+   str(UNIT_COSTS[playernumber][1]),  fontsize20,   colors[1])
    placeText(x, y + line_distance*3, "Robot    f",+   str(UNIT_COSTS[playernumber][2]),  fontsize20,   colors[1])
    placeText(x, y + line_distance*4, "Boat     f",+   str(UNIT_COSTS[playernumber][3]),   fontsize20,   colors[1])
    placeText(x, y + line_distance*5, "Barak    f",+   str(UNIT_COSTS[playernumber][4]),  fontsize20,   colors[1])
    
    if x < 15:
        x = x + 3.5
    else:
        x = x - 1.5
    y = y + 0.8
    player = player_list[playernumber]
    unitsNotOnBoard(x, y, soldiers[playernumber], playernumber.player.soldier)
    unitsNotOnBoard(x, y + line_distance, tanks[playernumber], playernumber,player.tank)
    unitsNotOnBoard(x, y + line_distance*2, robots[playernumber], playernumber,player.robot)
    unitsNotOnBoard(x, y + line_distance*3, boats[playernumber], playernumber,player.boat)
    unitsNotOnBoard(x, y + line_distance*4, barracks[playernumber], playernumber,player.barrack)

def addPlayers():
    global hover_list, player_list
    hover_list = [ [], [], [], [] ]
    player_list = []
    for playernumber in range(4):
        player_list.append( Player(playernumber, COLOR_LIST[playernumber], UNIT_COST[playernumber]) )
        unitImages = [soldier[playernumber],robots[playernumber], tank[playernumber,boat[playernumber],]]
        buildMenu(playernumber)
        

#def turn(number):
    

def init():
    global activePlayer
    activePlayer = 0

    pygame.init()
    pygame.display.init()
    
    drawGUI()
    loadImages()
    addPlayers()

    pygame.display.set_caption('frequency Game')
    pygame.display.flip()


def Main():
    init()

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for hover_item in hover_list[activePlayer]:
            hover_item.Update()

        cur = pygame.mouse.get_pos()



        pygame.display.update()

if __name__== "__main__":
Main()
