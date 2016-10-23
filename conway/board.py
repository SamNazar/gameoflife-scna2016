class Board():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.grid = [[False for _ in range(self.height)] for _ in range(self.width)] 

	def giveLife(self, x, y):
		self.grid[x][y] = True
	
	def takeLife(self, x, y):
		self.grid[x][y] = False
	
	def isValid(self, x, y):
		return ((0 <= x < self.width) and (0 <= y < self.height))

	def countLivingNeighbors(self, x, y):
		count = 0
		if (self.isValid(x-1, y-1) and self.grid[x-1][y-1]): count += 1
		if (self.isValid(x-1, y) and self.grid[x-1][y]): count += 1
		if (self.isValid(x-1, y+1) and self.grid[x-1][y+1]): count += 1
		if (self.isValid(x, y-1) and self.grid[x][y-1]): count += 1
		if (self.isValid(x, y+1) and self.grid[x][y+1]): count += 1
		if (self.isValid(x+1, y-1) and self.grid[x+1][y-1]): count += 1
		if (self.isValid(x+1, y) and self.grid[x+1][y]): count += 1
		if (self.isValid(x+1, y+1) and self.grid[x+1][y+1]): count += 1
		return count

	def __str__(self):
		strRepr = ""
		transposedGrid = zip(*self.grid)
		for row in transposedGrid:
			for cell in row:
				if cell:
					strRepr += "##"
				else:
					strRepr += ".."
			strRepr += "\n"
		return strRepr