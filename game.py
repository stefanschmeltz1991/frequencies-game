import sys, webbrowser

from board import *












RED             = [ (102,0,0), (128,0,0), (178,34,34) ]
GREEN           = [ (0,51,0), (0,100,0), (0,128, 0) ]
BLUE            = [ (0,0,128),(0,0,205) , (65,105,225) ]
YELLOW          = [ (218,165,32), (255,215,0 ), (240,230,140) ]


class Game:
    def __init__(self):
        self.COLOR_LIST = [ RED, BLUE, YELLOW, GREEN ]
        self.UNIT_COSTS = [ [ 150, 300, 750, 500,  800 ], \
                            [ 120, 300, 750, 500, 1000 ], \
                            [ 150, 300, 600, 500, 1000 ], \
                            [ 150, 240, 750, 500, 1000 ] ]
        self.quit           = False
        self.selectedSquare = None
        self.selectedUnit   = None
        self.purchasedUnit  = None
        self.buying         = False
        self.attacking      = False
        self.gameOver       = False
        self.reset          = False

        self.frequency      = Frequency(self)
        self.board          = Board(self)
        self.frequency.placeInitialBases()
        self.displayPlayerMove(self.frequency.activePlayer)

        
        while not self.quit == True:
            self.mainLoop()

        if self.reset:
            self.__init__()

    def mainLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:#restart the game
                if event.key == pygame.K_r:
                    self.reset = True
                    self.quit = True
            if event.type == pygame.KEYDOWN:#restart the game
                if event.key == pygame.K_x:
                    webbrowser.open_new("file://" + os.path.realpath("Manual.pdf"))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True

            elif not self.gameOver:
                self.board.update(event)


    
    def selectBoardSquareAction(self, square):
        if self.attacking:
            self.frequency.tryAttack(square)
            self.attacking = False
        elif self.purchasedUnit is not None:
            self.frequency.tryPlaceUnit(square, self.purchasedUnit)
            self.selectedSquare = None
        elif self.selectedSquare is None:
            self.selectedSquare = square
            self.board.displayMessage("Selected square (" + str(square.x) + "," + str(square.y) + ")")
        else:
            if self.frequency.moveAllowed(self.selectedSquare, square):
                # unit verplaatsen van het vierkant waar eerder op geklikt was naar het vierkant waar nu op wordt geklikt

                self.frequency.moveUnit(self.selectedSquare, square)
                self.selectedSquare = None
            elif self.frequency.moveOntoBoatAllowed(self.selectedSquare, square):
                # unit op boat plaatsen
                #place units on the boat
                self.frequency.moveUnitOntoBoat(self.selectedSquare, square)
                self.selectedSquare = None
            elif self.frequency.moveOffBoatAllowed(self.selectedSquare, square):
                self.frequency.moveUnitOffBoat(self.selectedSquare, square)
                self.selectedSquare = None
            else:
                self.selectedSquare = square
                self.board.displayMessage("Selected square (" + str(square.x) + "," + str(square.y) + ")")
            

    def buyAction(self, button):
        if self.purchasedUnit is not None:
            self.board.displayMessage("Place " + self.purchasedUnit.name + " on board first")
        else:
            if self.selectedUnit is not None:
                self.buyUnit()
                self.klick()
            else:
                self.buying = True
                self.board.displayMessage("Select the unit you want to buy")            
        
    def attackAction(self, button):
        if self.purchasedUnit is not None:
            self.board.displayMessage("Place " + self.purchasedUnit.name + " before attacking")
        elif self.selectedSquare is not None and self.selectedSquare.getPlayer() != self.frequency.getActivePlayer:
            self.frequency.tryAttack(self.selectedSquare)
            self.attacking = False
            self.selectedSquare = None
        else:
            self.attacking = True
            self.board.displayMessage("Choose a square to attack")
            #self.fightsound()
    def nextAction(self, button):
        if self.purchasedUnit is not None:
            self.board.displayMessage("Place " + self.purchasedUnit.name + " on board first")
        else:
            self.klick()
            self.selectedUnit = None
            self.selectedSquare = None

            if button is not None:
                button.hover = False
                button.reset()
            self.frequency.nextPlayer()
            self.board.showMoney(self.frequency.activePlayer)
            

    def displayPlayerMove(self, playerNumber):
        land = LAND_TYPE[playerNumber]
        self.board.displayMessage(land + " is on the move")

    def unitSelectedAction(self, button):
        self.selectedUnit = button.unit
        if self.buying:
            self.buyUnit()
        else:
            self.board.displayMessage("Unit " + self.selectedUnit.name + " f" + str(self.selectedUnit.price))

    def buyUnit(self):
        self.buying = False
        if self.frequency.getActivePlayer().buy(self.selectedUnit):
            self.purchasedUnit = self.selectedUnit
            self.selectedUnit = None
            self.board.showMoney(self.frequency.activePlayer)      
            self.board.displayMessage("purchased " + self.purchasedUnit.name + " for f" + str(self.purchasedUnit.price))
            self.coinsSound()
        else:
            self.board.displayMessage("Insufficient funds")

     ######## SOUND EFFECTS ##################
    def fightsound(self):
        fight = pygame.mixer.Sound('fight.wav')
        pygame.mixer.Sound.play(fight)
        fight.set_volume(0.2)
    def stepSound(self):
        step = pygame.mixer.Sound('stepSFX.wav')
        pygame.mixer.Sound.play(step)
        step.set_volume(0.2)
    def coinsSound(self):
        step = pygame.mixer.Sound('coins.wav')
        pygame.mixer.Sound.play(step)
        step.set_volume(0.2)

    def klick(self):
        step = pygame.mixer.Sound('klick.wav')
        pygame.mixer.Sound.play(step)
        step.set_volume(0.2)

def main():
    Game()


if __name__ == "__main__":
    main()

