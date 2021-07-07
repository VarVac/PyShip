import random

#construct a battleship grid and place a battleship by marking four adjacent spaces as containing the battleship. When the battleship is hit, mark the battleship space as "HIT"
class Battleship():

    #init takes rows and columns
    def __init__(self, gridSize, shipSize):
        #number of hits
        self.numHits = 0
        
        #save shipSize
        self.shipSize = shipSize

        #ship status
        self.isSunk = False

        #genarate a square grid
        self.grid = [[0 for i in range(gridSize)] for j in range(gridSize)]
        #print(self.grid)

        #define the direction to place the rest of the battleship
        placeCase = random.randrange(2)
        placeVector = self.createPlaceVector(placeCase)
        #print(placeVector)

        #define a location for the first battleship space
        placeLocation = self.createPlaceLocation(placeCase, gridSize, shipSize)
        #print(placeLocation)


        #place the battleship
        self.placeBattleShip(placeLocation[0], placeLocation[1], placeVector[0], placeVector[1], shipSize-1)
        #print(self.grid)
        
    #generates a place vector
    #generate 4 possible vectors (1,0), (0,1), (-1,0), (0,-1)
    def createPlaceVector(self, placeCase):
        #+x
        if placeCase == 0:
            return (1,0)
        #+y
        elif placeCase == 1:
            return (0,1)

    #generates the placeLocation, must consider the placeCase ((1,0), (0,1), (-1,0), or (0,-1)) and size to avoid invalid configurations
    def createPlaceLocation(self, placeCase, gridSize, shipSize):
        #+x: x must be between 0 to gridSize - shipSize (inclusive)
        if placeCase == 0:
            return (random.randint(0, gridSize - shipSize),random.randrange(gridSize))
        #+y: y must be between 0 to gridSize - shipSize
        elif placeCase == 1:
            return (random.randrange(gridSize),random.randint(0, gridSize - shipSize))

    #place the battleship by setting a grid location to 1
    #function recursively calls itself until length is 0, each time, change the placeLocation by adding the place vector
    def placeBattleShip(self, placeLocationX, placeLocationY, placeVectorX, placeVectorY, length):
        #print("Place")
        self.grid[placeLocationX][placeLocationY] = 1

        #if length is not 0, recur to place the next space
        #add the placeVector to the placeLocation to get the next placeLocation
        if(length != 0):
            self.placeBattleShip(placeLocationX + placeVectorX, placeLocationY + placeVectorY, placeVectorX, placeVectorY, length-1)

    #Check grid for a hit, if hit, return 1, if miss, return 0
    def fire(self, fireX, fireY):
        if self.grid[fireX][fireY] == 1:
            self.hit()
            return 1
        else:
            self.miss()
            return 0

    #what to do if hit
    def hit(self):
        self.numHits += 1
        #print(self.numHits)
        print('hit')
        self.checkSunk()

    #what to do on a miss
    def miss(self):
        print('miss')

    #check if sunk
    def checkSunk(self):
        if self.numHits == self.shipSize:
            self.sunk()

    #what to do if sunk
    def sunk(self):
        self.isSunk = True
        print('You sunk my Battleship!')

testBattleship = Battleship(5,4)
testBattleship.fire(2,2)
testBattleship.fire(2,3)
testBattleship.fire(2,4)
testBattleship.fire(2,1)

testBattleship.fire(1,2)
testBattleship.fire(2,2)
testBattleship.fire(3,2)
testBattleship.fire(4,2)