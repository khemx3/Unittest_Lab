import unittest

from hex import *



class CaseCheck(unittest.TestCase):
    def testUpper(self):
        for integer in range(1, 3999):
            h = toHex(integer)
            self.assertEqual(h, h.upper())


if __name__ == "__main__":
    unittest.main()