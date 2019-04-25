import unittest
# import binsearch as binary
from binsearch import *


class BinSearchBadInput(unittest.TestCase):
    def testInvalidInput(self):
        self.assertRaises(InvalidArgument, binsearch, '12345', 1)
        

if __name__ == "__main__":
    unittest.main()