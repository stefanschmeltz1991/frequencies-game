import time
import os, pygame




#Het spelbord is een vierkant bord. Elke hoek van het bord heeft zijn eigen basis met zijn eigen klimaat.
#In het midden van het bord bevindt zich de goudmijn. Tussen de gebieden bevindt zich water.
#Het bord is opgedeeld in vakjes.

#Per vakje in je eigen gebied krijg je f 50,

#per vakje dat je in vijandelijk gebied hebt krijg je f 100

#in de goudmijn f 150 per vakje.

#Aan de randen van het spelbord staat een legenda die je ondersteunt tijdens het spelen van het spel.
#In het eerste vakje van je eigen gebied, voor het moeras dus in de linkerbovenhoek,
#bevindt zich een barak die dienst doet als basis waaruit het spel begint.

#Binnen het spel heb je beurten.
# In deze beurten krijg je 4 zetten,
# waarmee je acties kan laten plaatsvinden.
#  Acties zijn troepen maken, troepen verplaatsen, aanvallen doen en barakken bouwen.
#  Troepen maken kost 1 zet. Troepen verplaatsen kost 1 zet. Aanvallen kost 1 zet en barakken bouwen kost 1 zet. Je kunt geen zetten opsparen.
#  Dit betekent dus dat als je een zet niet gebruikt je deze niet later kunt gebruiken.
# Als je een zet gedaan hebt kun je deze niet meer terugdraaien.
# Ook kan je geen zetten aan andere spelers geven.
# Ook geldt de regel aanraken is zetten.
class Unit:

    def __init__(self, name, power,price, image):
        self.name   = name
        self.power  = power
        self.image  = image
        self.price  = price
        self.costs  = costs

class soldier(Unit,costs, image):
    def __init__(self):
        Unit.__init__(self, 'soldier', 1, image)

class Robot(Unit,costs, image):
        def __init__(self):
            Unit.__init__(self, 'robot', 2, image)

class Tank(Unit,costs, image):
         def __init__(self):
            Unit.__init__(self, 'tank', 3, image)

class Barrack(Unit,costs, image):
         def __init__(self):
            Unit.__init__(self, 'baraack', 6, image)
class Boat(Unit, costs, image):
         def __init__(self):
            Unit.__init__(self, 'boat', 6, image)

class Player:

    def __init__(self,colors, unitCost):
        self.landType       = landType
        self.Money          = 10000    # Elke speler begint met f10.000
        self.soldier        = Soldier(unitImagges[0])
        self.Robot          = Robot(unitImagges[1])
        self.Tank           = Tank(unitImagges[2])
        self.Barak          = Barak(unitImagges[3])
        self.Boat           = Boat(unitImagges[4])

        self.colors         = colors
        self.unitCosts      = {'soldier': unitCost[0], \
                              'robot':    unitCost[1],\
                              'tank':     unitCost[2],\
                               'barack':  unitCost[3],
                               'boat':    unitCost[4]}

        self.Units          =[]
        self.pricelist      = []

        self.island         =''
        #___________UNITS COST____________#
        self.barrackcost    = 500       # kost f500
        self.harborcost     = 600       # kost f600
        self.soldiercost    = 150       # kost 150
        self.robotcost      = 300       # kost 300
        self.tankcost       = 750       # kost 750
        self.boatcost       = 1000      # kost 1000

##        if playercolor == "RED":
##            self.barrackLocation = 1,18
##            self.Playernumber = 4
##            self.tankCost = 600
##            self.Island = 'desert'
##
##            self.barrackText = pygame.image.load(os.path.join("assets", "bluebar.png")).convert_alpha()
##            self.harborText = pygame.image.load(os.path.join("assets", "blueharbor.png")).convert_alpha()
##
##
##
##        elif playercolor == "GREEN":
##            self.barrackLocation = 1,1
##            self.barrackText = pygame.image.load(os.path.join("assets", "greenbar.png")).convert_alpha()
##            self.harborText = pygame.image.load(os.path.join("assets", "greenharbor.png")).convert_alpha()
##            self.Island = 'forest'
##            self.Playernumber = 3
##            self.barrackCost = 450
##            self.boatCost = 800
##
##
##        elif playercolor == "BLUE":
##            self.barrackLocation = 18,1
##            self.barrackText = pygame.image.load(os.path.join("assets", "bluebar.png")).convert_alpha()
##            self.harborText = pygame.image.load(os.path.join("assets", "blueharbor.png")).convert_alpha()
##            self.Island = 'ice plains'
##            self.Playernumber = 2
##            self.soldierCost = 120
##
##        elif playercolor == "YELLOW":
##            self.barrackLocation = 18,18
##            self.barrackText = pygame.image.load(os.path.join("assets", "yellowbar.png")).convert_alpha()
##            self.harborText = pygame.image.load(os.path.join("assets", "yellowharbor.png")).convert_alpha()
##            self.Island = 'forest'
##            self.Playernumber = 1
##            self.colorRGB = (51,255,51)
##            self.robotCost = 240





class Unit:

    def __init__(self, typeofunit, power, price): #location is a tuple
        self.typeOfUnit= type
        self.Power = power
        self.Price = price


##        if team == 'RED':
##            if typeofunit           == 'soldier':
##                self.Text           = pygame.image.load(os.path.join( "redsoldier.png")).convert_alpha()
##                self.Powervalue     = 1
##            if typeofunit           == 'robot':
##                self.Text           = pygame.image.load(os.path.join( "redrobot.png")).convert_alpha()
##                self.Powervalue     = 2
##            if typeofunit           == 'tank':
##                self.Text           = pygame.image.load(os.path.join ("redtank.png")).convert_alpha()
##                self.Powervalue     = 3
##            if typeofunit           == 'boat':
##                self.Text           = pygame.image.load(os.path.join( "redboat.png")).convert_alpha()
##                self.Powervalue     = 6
##
##                self.Soldiercount   = 0
##                self.Robotcount     = 0
##                self.Tankcount      = 0
##        if team == 'BLUE':
##            if typeofunit           == 'soldier':
##                self.Text = pygame.image.load(os.path.join( "bluesoldier.png")).convert_alpha()
##                self.Powervalue     = 1
##            if typeofunit           == 'robot':
##                self.Text           = pygame.image.load(os.path.join( "bluerobot.png")).convert_alpha()
##                self.Powervalue     = 2
##            if typeofunit           == 'tank':
##                self.Text           = pygame.image.load(os.path.join( "bluetank.png")).convert_alpha()
##                self.Powervalue     = 3
##            if typeofunit           == 'boat':
##                self.Text           = pygame.image.load(os.path.join( "blueboat.png")).convert_alpha()
##                self.Powervalue     = 6
##
##                self.Soldiercount   = 0
##                self.Robotcount     = 0
##                self.Tankcount      = 0
##        if team == 'YELLOW':
##            if typeofunit           == 'soldier':
##                self.Text           = pygame.image.load(os.path.join( "yellowsoldier.png")).convert_alpha()
##                self.Powervalue     = 1
##            if typeofunit           == 'robot':
##                self.Text           = pygame.image.load(os.path.join( "yellowrobot.png")).convert_alpha()
##                self.Powervalue     = 2
##            if typofunite           == 'tank':
##                self.Text           = pygame.image.load(os.path.join( "yellowtank.png")).convert_alpha()
##                self.Powervalue     = 3
##            if typeofunit           == 'boat':
##                self.Text           = pygame.image.load(os.path.join( "yellowboat.png")).convert_alpha()
##                self.Powervalue     = 6
##
##                self.Soldiercount   = 0
##                self.Robotcount     = 0
##                self.Tankcount      = 0
##        if team == 'GREEN':
##            if typeofunit           == 'soldier':
##                self.Text           = pygame.image.load(os.path.join( "greensoldier.png")).convert_alpha()
##                self.Powervalue     = 1
##            if typeofunit           == 'robot':
##                self.Text           = pygame.image.load(os.path.join( "greenrobot.png")).convert_alpha()
##                self.Powervalue     = 2
##            if typeofunit           == 'tank':
##                self.Text           = pygame.image.load(os.path.join( "greentank.png")).convert_alpha()
##                self.Powervalue     = 3
##            if typeofunit           == 'boat':
##                self.Text           = pygame.image.load(os.path.join( "greenboat.png")).convert_alpha()
##                self.Powervalue     = 6
##
##                self.Soldiercount   = 0
##                self.Robotcount     = 0
##                self.Tankcount      = 0
##
##
##
###_______BUY UNITS & ADDING AMOUNT OF MONEY__________#
##    def changeMoney(self, amount): #positive number adds, negative number subtracts
##        self.Money += amount
##    def BuyUnit(self, loc, type):
##       self.Units.append(Unit(type, loc, self.Color))
##
##
###___________________MOVE DIRECTIONS__________________________#
##    def PlayerMove(self,direction):
##        if direction == 'left':
##            self.x = self.x - 1
##        if direction == 'right':
##            self.x = self.x + 1
##        if direction == 'up':
##            self.y = self.y - 1
##        if direction == 'down':
##            self.y = self.y + 1
##
##    def EliminateUnit(self, unit):
##        self.Units.remove(unit)  #When unit killed, remove unit from the board



class Land:
    def __init__(self, type, location, isBase): #location is a tuple
        self.Isbase = isBase
        self.Type = type
        self.x = location[0]
        self.y = location[1]
        self.occupied = False
        self.onIsland = ''
        self.Fortitude = 0

        if 7 < self.x < 12 and 7 < self.y < 12:
            self.onIsland =  'goldmine'
        if (self.x < 7 and self.y < 7) or  (self.x < 8 and self.y < 6) or (self.y < 8 and self.x < 6):
            self.onIsland =  'swamp'
        if (self.x > 12 and self.y < 7) or (self.x > 11 and self.y < 6) or (self.x > 13 and self.y < 8):
            self.onIsland =  'tundra'
        if (self.y > 12 and self.x < 7) or (self.y > 11 and self.x < 6) or (self.y > 13 and self.x < 8):
            self.onIsland =  'desert'
        if (self.x > 12 and self.y > 12) or  (self.x > 13 and self.y > 11) or (self.y > 13 and self.x > 11):
            self.onIsland =  'forest'

        if self.Type == 'harbor':
            self.Fortitude = 6
        if self.Type == 'barrack':
            self.Fortitude = 6
        if self.Type == 'headquarters':
            self.Fortitude = 25
