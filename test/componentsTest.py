from src.components import *
import unittest

#class TileTests(unittest.TestCase):
    #def (self):

class BoardTests(unittest.TestCase):
    def testCreateBoardNotNone(self):
        testBoard = Board()
        self.assertIsNotNone(testBoard)

#    def testBoardNotOutOfBounds(self):
#        testBoard = Board()
#        self.assertRaises()
