import time
import os, pygame

INITIAL_MONEY = 4000# 500


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
    def __init__(self, player, name, power, price, image):
        self.name = name
        self.power = power
        self.price = price
        self.image = image
        self.player = player
        
class Soldier(Unit):
    def __init__(self, player, price, image):
        Unit.__init__(self, player, 'soldier', 1, price, image)


class Robot(Unit):
    def __init__(self, player, price, image):
        Unit.__init__(self, player, 'robot', 2, price, image)

class Tank(Unit):
    def __init__(self, player, price, image):
        Unit.__init__(self, player, 'tank', 3, price, image)

class Barrack(Unit):
    def __init__(self, player, price, image):
        Unit.__init__(self, player, 'barrack', float(0.5), price, image)

class Boat(Unit):
    def __init__(self, player, price, image):
        self.unitOnBoat = None
        Unit.__init__(self, player, 'boat', 6, price, image)

    
class Player:
    def __init__(self, colors, unitCosts, unitImages):
        self.money   = INITIAL_MONEY
        self.soldier = Soldier(self, unitCosts[0], unitImages[0])
        self.robot   = Robot(self, unitCosts[1], unitImages[1])
        self.tank    = Tank(self, unitCosts[2], unitImages[2])
        self.barrack = Barrack(self, unitCosts[3], unitImages[3])
        self.boat    = Boat(self, unitCosts[4], unitImages[4])

        self.colors = colors
        self.baseSquare = None
        self.alive      = True

    def addMoney(self, amount):
        self.money = self.money + amount
        
    def buy(self, unit):
        if self.money > unit.price:
            self.money = self.money - unit.price
            return True
        else:
            return False
        
