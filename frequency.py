from player import *


NUMBER_OF_MOVES_PER_TURN    = 40  # 4
WIN_TARGET                  = 50000            # 50000
COLOR_NAMES                 = [ "red", "blue", "yellow", "green"]
LAND_TYPE                   = [ "Swamp", "Ice plains", "Desert",  "Forrest", "Goldmine" ]


class Frequency:
    
    def __init__(self, game):
        self.game = game
        self.addPlayers()
        self.activePlayer = 3
        self.numberOfMoves = 0

    def placeBase(self, player, square):
        player.baseSquare   = square
        unit                = Barrack(player, 0, player.barrack.image)
        unit.power          = 2    # basis heeft meer verdedigingspunten dan een gewone barak
        square.placeUnit(unit)
        
    def placeInitialBases(self):
        self.placeBase(self.nextPlayer(), self.game.board.boardSquares[0][0])
        self.placeBase(self.nextPlayer(), self.game.board.boardSquares[17][0])
        self.placeBase(self.nextPlayer(), self.game.board.boardSquares[0][17])
        self.placeBase(self.nextPlayer(), self.game.board.boardSquares[17][17])
    # in this function we create for player, wich going to be added in the def adPlayers funtion
    def addPlayers(self):
        self.player_list = []
        for i in range(4):
            self.addPlayer(i)
    #the 4 player are added in this function. each player receive his own color, the price of his units and the units images.
    def addPlayer(self, playerNumber):
        self.player_list.append( Player(self.game.COLOR_LIST[playerNumber],#the color of each player menu
                                        self.game.UNIT_COSTS[playerNumber],#the cost of the units of eachr player
                                        self.loadUnitImages(playerNumber)) )#the units images in different colors
    #in this loop, all the units images are loaded here in different colors
    def loadUnitImages(self, playerNumber):
        color = COLOR_NAMES[playerNumber]
        images = []
        images.append(pygame.image.load(os.path.join( color + "soldier.png")))
        images.append(pygame.image.load(os.path.join( color + "robot.png")))
        images.append(pygame.image.load(os.path.join( color + "tank.png")))
        images.append(pygame.image.load(os.path.join( color + "bar.png")))
        images.append(pygame.image.load(os.path.join( color + "boat.png")))
        images.append(pygame.image.load(os.path.join( color + "harbor.png")))
        return images
 
    def updateNumberOfMoves(self):#every move of a player is updated in this function, if the number reaches a certain amount of moves, than the it wil be directed to the which will automaticly change the players turn
        self.numberOfMoves = self.numberOfMoves + 1
        if self.numberOfMoves == NUMBER_OF_MOVES_PER_TURN:
            self.game.nextAction(None)

    def gameOver(self):
        self.game.board.displayWiningMessage3(LAND_TYPE[self.activePlayer] + " has won!") # it will show a winning screen
        self.game.gameOver = True # when this is true, than game can no longer be played.
            
    def nextPlayer(self):
        # werkt nu voor vier spelers
        self.activePlayer   = (self.activePlayer + 1) % 4
        self.numberOfMoves  = 0;#number of moves returns to zero
        player              = self.getActivePlayer()

        if player.alive:
            self.game.displayPlayerMove(self.activePlayer)
            self.incomePlayer()
            if player.money >= WIN_TARGET:
                self.gameOver()
            return player
        else:
            return self.nextPlayer()

    def getActivePlayer(self):
        return self.player_list[self.activePlayer]

    def checkNumberOfPlayersAlive(self):
        alive = 0
        for player in self.player_list:
            if player.alive:
                alive = alive + 1
        if alive == 1:
            self.gameOver()

    def removePlayer(self, player):
        self.getActivePlayer().addMoney(player.money)
        for i in range(18):
            for j in range(18):
                square = self.game.board.boardSquares[i][j]
                if square.getPlayer() == player:
                    square.removeUnit()
        player.money = 0
        player.alive = False
        self.checkNumberOfPlayersAlive()
        
    def attack(self, square, power):
        if square.unit.power <= power:
            for player in self.player_list:
                if square == player.baseSquare and player.alive:
                    self.removePlayer(player)
            square.removeUnit2()
        
    def attackPower(self, square):
        power = 0
        for x in range(max(1, square.x - 2), 1 + min(18, square.x + 2)):
            for y in range(max(1, square.y - 2), 1 + min(18, square.y + 2)):
                s = self.game.board.boardSquares[x-1][y-1]
                if s.getPlayer() == self.getActivePlayer():

                    if isinstance(s.unit, Soldier) and s.distance(square) == 1:#r the isinstance function return whether an object is an instance of a class or of a subclass thereof.
                                                                                #With a type as second argument, return whether that is the object's type.
                        power = power + s.unit.power
                        print(power)
                    if isinstance(s.unit, Robot) and s.distance(square) == 1:
                        power = power + s.unit.power
                        print(power)
                    if isinstance(s.unit, Barrack) and s.distance(square) <= 1:
                        power = power + s.unit.power
                        print(power)


                    if isinstance(s.unit, Tank):
                        power = power + s.unit.power
        return power

        
    def tryAttack(self, square):

        if square.isEmpty():
            self.game.board.displayMessage("Nothing to attack on (" + str(square.x) + "," + str(square.y) + ").")
        elif square.getPlayer() == self.getActivePlayer():
            self.game.board.displayMessage("Cannot attack your")
            self.game.board.displayMessage2("own unit or building,")
        else:
            power = self.attackPower(square)
            if power == 0:
                self.game.board.displayMessage("No units nearby to attack (" + str(square.x) + "," + str(square.y) + ").")
            else:
                self.game.board.displayMessage("Attacking square (" + str(square.x) + "," + str(square.y) + ")")
                self.attack(square, power)
                self.updateNumberOfMoves()
                self.game.fightsound()
    def placeUnit(self, square, unit):
        if square.isEmpty():
            self.game.board.displayMessage(unit.name + " placed (" + str(square.x) + "," + str(square.y) + ").")
            square.placeUnit(unit)
            self.game.board.placeUnit(square.x, square.y, unit.image)
            self.game.purchasedUnit = None
            self.updateNumberOfMoves()
        else:
            self.game.board.displayMessage("Insufficient space here")
            self.game.board.displayMessage2("Purchase canceld.")
            self.cancelPurchase()

    def moveUnit(self, fromSquare, toSquare):
        toSquare.placeUnit(fromSquare.unit)
        self.game.stepSound()
        fromSquare.removeUnit()
        self.updateNumberOfMoves()


    def moveAllowed(self, fromSquare, toSquare):
        if fromSquare.isEmpty():
            return False
        if not toSquare.isEmpty():
            return False
        if fromSquare.getPlayer() != self.getActivePlayer():
            return False
        if fromSquare == toSquare:
            return False
        
        unit = fromSquare.unit
        distance = fromSquare.distance(toSquare)
        if isinstance(unit, Soldier) and distance <= 1 and toSquare.isLand():                
            return True
        if isinstance(unit, Robot) and distance <= 1 and toSquare.isLand():                
            return True
        if isinstance(unit, Tank) and distance <= 2 and toSquare.isLand():
            return True
        if isinstance(unit, Boat) and distance <= 3 and toSquare.isWater():
            return True       
        
        return False

    def moveUnitOntoBoat(self, fromSquare, toSquare):
        toSquare.moveOntoBoat(fromSquare.unit)
        fromSquare.removeUnit()
        self.updateNumberOfMoves()

    def moveOntoBoatAllowed(self, fromSquare, toSquare):
        if fromSquare.getPlayer() != self.getActivePlayer():
            return False
        if toSquare.getPlayer() != self.getActivePlayer():
            return False
        if fromSquare == toSquare:
            return False
        if not toSquare.isEmptyBoat():
            return False
        
        unit = fromSquare.unit
        distance = fromSquare.distance(toSquare)
        if isinstance(unit, Soldier) and distance <= 1:                
            return True
        if isinstance(unit, Robot) and distance <= 1:                
            return True
        if isinstance(unit, Tank) and distance <= 2:
            return True

        return False

    def moveUnitOffBoat(self, fromSquare, toSquare):
        toSquare.placeUnit(fromSquare.unit.unitOnBoat)
        fromSquare.removeUnitFromBoat()
        self.updateNumberOfMoves()

    def moveOffBoatAllowed(self, fromSquare, toSquare):
        if fromSquare.getPlayer() != self.getActivePlayer():
            return False
        if not toSquare.isEmpty():
            return False
        if fromSquare == toSquare:
            return False
        if not fromSquare.hasBoat() or fromSquare.isEmptyBoat():
            return False
        
        unit = fromSquare.unit.unitOnBoat
        distance = fromSquare.distance(toSquare)
        if isinstance(unit, Soldier) and distance <= 1:                
            return True
        if isinstance(unit, Robot) and distance <= 1:                
            return True
        if isinstance(unit, Tank) and distance <= 2:
            return True

        return False

    def nextToLandUnit(self, square):
        for x in range(max(1, square.x - 1), 1 + min(18, square.x + 1)):
            for y in range(max(1, square.y - 1), 1 + min(18, square.y + 1)):
                s = self.game.board.boardSquares[x-1][y-1]
                if square != s and s.isLand() and s.getPlayer() == self.getActivePlayer():
                    return True
        return False

    def nextToBarrack(self, square):
        for x in range(max(1, square.x - 1), 1 + min(18, square.x + 1)):
            for y in range(max(1, square.y - 1), 1 + min(18, square.y + 1)):
                s = self.game.board.boardSquares[x-1][y-1]
                if s.hasBarrack() and s.getPlayer() == self.getActivePlayer():
                    return True
        return False

    def cancelPurchase(self):
        self.getActivePlayer().addMoney(self.game.purchasedUnit.price)
        self.game.board.showMoney(self.activePlayer)
        self.game.purchasedUnit = None


    def tryPlaceBarrack(self, square, barrack):
        if square.isWater():
            self.game.board.displayMessage("Can't place a barrack on water.")
        elif self.nextToLandUnit(square):
            self.placeUnit(square, barrack)
        else:
            self.game.board.displayMessage("Too far from your land units.")

    def tryPlaceBoat(self, square, boat):
        if square.isLand():
            self.game.board.displayMessage("Can't place a boat on land.")
        elif self.nextToLandUnit(square):
            self.placeUnit(square, boat)
        else:
            self.game.board.displayMessage("Too far from your land units.")
            self.game.board.displayMessage2("Purchase canceld")
            self.cancelPurchase()

    def tryPlaceSoldierRobotTank(self, square, unit):
        if square.isWater():
            self.game.board.displayMessage("Can't place a " + unit.name + " on water.")
        if self.nextToBarrack(square):
            self.placeUnit(square, unit)
        else:
            self.game.board.displayMessage("Too far from barrack.")
        
    def tryPlaceUnit(self, square, unit):
        if isinstance(unit, Barrack):
            self.tryPlaceBarrack(square, unit)                   
        elif isinstance(unit, Boat):
            self.tryPlaceBoat(square, unit)                   
        else:
            # unit is a soldier, robot or tank
            self.tryPlaceSoldierRobotTank(square, unit)
     
        
    def incomePlayer(self):
        # inkomen bepalen voor de speler die aan de beurt is
        income = 0
        for i in range(18):
            for j in range(18):
                square = self.game.board.boardSquares[i][j]
                if square.getPlayer() == self.getActivePlayer():
                    if square.landType == self.activePlayer:
                        income = income + 50
                    elif square.isGoldMine():
                        income = income + 150
                    elif square.isLand():
                        income = income + 100

        self.game.board.displayMessage2("player earned " + str(income) + " income.")
        self.getActivePlayer().addMoney(income)
    
                
