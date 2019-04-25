import unittest
from Circle import *


class CircleTest(unittest.TestCase):

    knownValues = [(1,6.283185307179586,3.141592653589793),
                (2,12.566370614359172,12.566370614359172),
                (3,18.84955592153876,28.274333882308138),
                (4,25.132741228718345,50.26548245743669),
                (5,31.41592653589793,78.53981633974483),
              
    ]

    knownXY = [(1, 1, 1, 1),
            (2, 2, 2, 2)
            ]
    def setUp(self):
        self.c = Circle()

    def testForParameter(self):
        for x, y, z in self.knownValues:
            self.c.setRadius(x)
            self.assertEqual(self.c.getPerimeter(), y)
            self.assertEqual(self.c.getArea(), z)

    def testZeroRadius(self):
        for x, y, z in self.knownValues:
            self.assertRaises(InvalidInputError, self.c.setRadius, 0)
    
    def testNegativeRadius(self):
        for x, y, z in self.knownValues:
            self.assertRaises(InvalidInputError, self.c.setRadius, -1)

    def testNewXY(self):
        for a, b, c, d in self.knownXY:
            self.assertEqual(self.c.move(a, b), (c, d))
    
    def testIntInput(self):
        for a, b, c, d in self.knownXY:
            self.assertEqual(type(self.c.getX()), int)
            self.assertEqual(type(self.c.getY()), int)
            
                



if __name__ == "__main__":
    unittest.main()

