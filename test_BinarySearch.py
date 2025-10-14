import unittest
from binarysearch import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_Found(self):
        numbers = [2,5,10,20,50,100]
        target = 5
        result = BinarySearch(numbers, target)
        self.assertTrue(result)
    def test_NotFound(self):
        numbers = list(range(0, 2000, 5))
        target = 723
        result = BinarySearch(numbers, target)
        self.assertFalse(result)
if __name__ == '__main__':
    unittest.main()