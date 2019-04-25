from hex import *
import unittest

class HexBadInput(unittest.TestCase):
    def testNegativeInput(self):
        self.assertRaises(InvalidArgument, toHex, -1)
    def testZeroInput(self):
        self.assertRaises(InvalidArgument, toHex, 0)
    def testNotInteger(self):
        self.assertRaises(InvalidArgument, toHex, 0.5)

if __name__ == "__main__":
    unittest.main()