import unittest
from MathUtils import *
class TestMathUtils(unittest.TestCase):
    def test_isEven(self):
        self.assertTrue(IsEven(10))
        self.assertFalse(IsEven(5))
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        with self.assertRaises(ValueError):
            factorial(-5)
    def test_MaxMin(self):
        self.assertEqual(MaxMin([1, 0, 10, -3, 5]), (10, -3))
if __name__ == '__main__':
    unittest.main()