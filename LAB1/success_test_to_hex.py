from hex import *
import unittest

class Knowvalues(unittest.TestCase):
    knowValues = (
        (265, '109'),
        (1103, '44F'),
        (775, '307'),
        (440, '1B8'),
        (490, '1EA'),
        (1528, '5F8'),
        (611, '263'),
        (1137, '471'),
        (185, 'B9'),
        (951, '3B7'),
        (695, '2B7'),
        (1668, '684'),
        (797, '31D'),
        (27, '1B'),
        (946, '3B2')
    )

    def testToHex(self):
        for decimal, result in self.knowValues:
            self.assertEqual(toHex(decimal), result)

if __name__ == '__main__':
    unittest.main()