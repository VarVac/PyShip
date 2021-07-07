import random

#construct a PyShip grid and place a PyShip by marking four adjacent spaces as containing the PyShip. When the PyShip is hit, mark the PyShip space as "HIT"
class PyShip():

    #init takes rows columns and number of tries
    def __init__(self, gridSize, shipSize, tries):
        #number of hits
        self.numHits = 0

        #number of tries
        self.tries = tries

        #save shipSize
        self.shipSize = shipSize

        #genarate a square grid
        self.grid = [[0 for i in range(gridSize)] for j in range(gridSize)]
        #print(self.grid)

        #define the direction to place the rest of the PyShip
        placeCase = random.randrange(2)
        placeVector = self.createPlaceVector(placeCase)
        #print(placeVector)

        #define a location for the first PyShip space
        placeLocation = self.createPlaceLocation(placeCase, gridSize, shipSize)
        #print(placeLocation)


        #place the PyShip
        self.placePyShip(placeLocation[0], placeLocation[1], placeVector[0], placeVector[1], shipSize-1)
        #print(self.grid)    
        
    #generates a place vector
    #generate 4 possible vectors (1,0), (0,1)
    def createPlaceVector(self, placeCase):
        #+x
        if placeCase == 0:
            return (1,0)
        #+y
        elif placeCase == 1:
            return (0,1)

    #generates the placeLocation, must consider the placeCase ((1,0), (0,1)) and size to avoid invalid configurations
    def createPlaceLocation(self, placeCase, gridSize, shipSize):
        #+x: x must be between 0 to gridSize - shipSize (inclusive)
        if placeCase == 0:
            return (random.randint(0, gridSize - shipSize),random.randrange(gridSize))
        #+y: y must be between 0 to gridSize - shipSize
        elif placeCase == 1:
            return (random.randrange(gridSize),random.randint(0, gridSize - shipSize))

    #place the PyShip by setting a grid location to 1
    #function recursively calls itself until length is 0, each time, change the placeLocation by adding the place vector
    def placePyShip(self, placeLocationX, placeLocationY, placeVectorX, placeVectorY, length):
        #print("Place")
        self.grid[placeLocationX][placeLocationY] = 1

        #if length is not 0, recur to place the next space
        #add the placeVector to the placeLocation to get the next placeLocation
        if(length != 0):
            self.placePyShip(placeLocationX + placeVectorX, placeLocationY + placeVectorY, placeVectorX, placeVectorY, length-1)

    #remove a try, Check grid for a hit, return the status of the hit and the game state
    def fire(self, fireX, fireY):
        self.tires -= 1

        #Check hit or miss
        if self.grid[fireX][fireY] == 1:
            self.hit(fireX,fireY)
            isHit = 'HIT'
            
        else:
            self.miss()
            isHit = 'MISS'

        #Check game state
        if self.checkSunk() == True:
            gameState = 'WIN'

        elif self.checkLost() == True:
            gameState = 'LOSE'
        
        else:
            gameState = 'CONT'
        
        return (isHit, gameState)

    #what to do if hit
    def hit(self,hitX,hitY):
        self.numHits += 1
        #print(self.numHits)
        self.grid[hitX][hitY] = 0
        print('hit')

    #what to do on a miss
    def miss(self):
        print('miss')

    #check if sunk
    def checkSunk(self):
        if self.numHits == self.shipSize:
            self.sunk()
            return True
        return False

    #check if game is lost
    def checkLost(self):
        if self.tries == 0:
            self.lose()
            return True
        return False

    #what to do if sunk
    def sunk(self):
        print('You sunk my PyShip!')

    #what to do if lose
    def lose(self):
        print ('You lost, sorry')