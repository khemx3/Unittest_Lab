import unittest

from binsearch import *

class IndexCheck(unittest.TestCase):
    def testIndexRange(self):
        arry = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for key in (0, len(arry)-1):
            index = binsearch(arry, key)
            self.assertTrue(0 <= index < len(arry))


class ValueCheck(unittest.TestCase):
    def testEqual(self):
        arry = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for key in (0, len(arry)-1):
            index = binsearch(arry, key)
            self.assertEqual(arry[index], key)

    def testNone(self):
        arry = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for key in (11, 20):
            index = binsearch(arry, key)
            self.assertEqual(index, None)


if __name__ == "__main__":
    unittest.main()
