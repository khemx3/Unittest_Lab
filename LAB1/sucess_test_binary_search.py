from binsearch import binsearch
import unittest


class KnowValues(unittest.TestCase):
    knowValues = (
        ([0, 1, 2, 3], 2, 2),
        ([], 1, None),
        ([0], 1, None),
        ([0, 1], -1, None),
        ([0, 3, 5], -10, None),
        ([0, 5, 9, 10], 1, None),
        ([1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 10], 1, 0),
        ([1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 10], 10, 14),
        ([1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 10], 11, None),
        ([0, 4, 7, 10, 20], 20, 4),
        ([0, 4, 7, 10, 20], 10, 3),
        ([0, 4, 7, 10, 20], 7, 2),
        ([0, 4, 7, 10, 20], 4, 1),
        ([0, 4, 7, 10, 20], 0, 0)
    )

    def testBinarySearch(self):
        for dataList, key, expected_result in self.knowValues:
            # print(dataList, key, expected_result)
            result = binsearch(dataList, key)
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
