import unittest
from conway import game
from conway import board

class TestGame(unittest.TestCase):
	
	def setUp(self):
		self.board = board.Board(12, 10)
		self.testgame = game.Game()

	def testAllDeadTicksToAllDead(self):
		newBoard = self.testgame.tick(self.board)
		for i in range(12):
			for j in range(10):
				self.assertFalse(newBoard.grid[i][j])

	def testSingleDisappears(self):
		self.board.giveLife(4, 5)
		newBoard = self.testgame.tick(self.board)
		self.assertFalse(newBoard.grid[4][5])
