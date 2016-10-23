from conway import board

class Game:

	def tick(self, prevBoard):
		newBoard = board.Board(prevBoard.width, prevBoard.height)
		for i in range(newBoard.width):
			for j in range(newBoard.height):
				newBoard.grid[i][j] = self.doesSurvive(prevBoard, i, j)
		return newBoard

	def doesSurvive(self, board, x, y):	
		livingNeighbors = board.countLivingNeighbors(x, y)
		cellIsAlive = board.grid[x][y]
		if (cellIsAlive):
			if (livingNeighbors < 2):
				return False # Rule 1: underpopulation
			elif (livingNeighbors > 3):
				return False # Rule 3: overpopulation
			else:
				return True # Rule 2: lives to the next generation
		else:
			if (livingNeighbors == 3):
				return True # Rule 4: reproduction
		return False # for dead cells that will remain dead 
