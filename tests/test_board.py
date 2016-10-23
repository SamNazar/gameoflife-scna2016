import unittest
from conway import board

class TestBoard(unittest.TestCase):

	def setUp(self):
		self.board = board.Board(12, 10)

	def testBoardHasWidthOf12(self):
		self.assertEqual(self.board.width, 12)

	def testBoardHasHeightOf10(self):
		self.assertEqual(self.board.height, 10)
	
	def testBoardStartsAllFalse(self):
		for i in range(12):
			for j in range(10):
				self.assertFalse(self.board.grid[i][j])

	def testBoardGivesCellLife(self):
		self.assertFalse(self.board.grid[3][4])
		self.board.giveLife(3, 4)
		self.assertTrue(self.board.grid[3][4])

	def testBoardTakesLife(self):
		self.board.giveLife(5, 7)
		self.assertTrue(self.board.grid[5][7])
		self.board.takeLife(5, 7)		
		self.assertFalse(self.board.grid[5][7])

	def testValidAndInvalidLocations(self):
		self.assertTrue(self.board.isValid(0, 0))
		self.assertFalse(self.board.isValid(0, 10))
	
	def testCountLivingNeighborsForNone(self):
		self.assertEqual(self.board.countLivingNeighbors(0, 4), 0)
		self.assertEqual(self.board.countLivingNeighbors(5, 5), 0)

	def testCountLivingNeighborsForSome(self):
		self.board.giveLife(5,5)
		self.board.giveLife(6,6)
		self.assertEqual(self.board.countLivingNeighbors(5, 5), 1)
		self.board.giveLife(4,5)
		self.assertEqual(self.board.countLivingNeighbors(5, 5), 2)
	

if __name__ == '__main__':
    unittest.main()