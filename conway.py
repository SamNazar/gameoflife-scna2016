from conway import game, board

aGame = game.Game()

totalTicks = 0

WIDTH = 32
HEIGHT = 16

# some shapes to play with
smallExploder = [(1, 0), (0, 1), (1, 1), (2, 1), (0, 2), (2, 2), (1, 3)]
exploder = [
	(0, 0), (2, 0), (4, 0),
	(0, 1), (4, 1), 
	(0, 2), (4, 2), 
	(0, 3), (4, 3), 
	(0, 4), (2, 4), (4, 4)
]
lightSpaceship = [(2, 6), (3, 6), (4, 6), (5, 6), (1, 7), (5, 7), (5, 8), (1, 9), (4, 9)]
glider = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]

def setupBoard(shapeWay, topLeftX, topLeftY):
	newBoard = board.Board(WIDTH, HEIGHT)
	for (x, y) in shapeWay:
		newBoard.giveLife(topLeftX + x, topLeftY + y)
	return newBoard

myBoard = setupBoard(exploder, 8, 4)

print("------INITIAL STATE------")
print(myBoard)

while (input("enter q to quit, anything else to continue: ") != "q"):
	myBoard = aGame.tick(myBoard)
	totalTicks += 1
	print("===== State after {0} ticks =====".format(totalTicks))
	print(myBoard)
