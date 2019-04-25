import unittest
from Calculator import *

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.c = Calculator(10)

    def testAdd(self):
        self.assertEqual(self.c.add(5), 15)
    
    def testSubtract(self):
        self.assertEqual(self.c.subtract(5), 5)

    def testMultiply(self):
        self.assertEqual(self.c.multiply(5), 50)

    def testDivide(self):
        self.assertEqual(self.c.divide(5), 2)

    def testDivideNotZero(self):
        self.assertRaises(InvalidInputError, self.c.divide, 0)

    def testString(self):
        self.assertRaises(StringInputError, self.c.add, 'asdads')
        

if __name__ == "__main__":
    unittest.main()