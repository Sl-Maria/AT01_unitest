import unittest
from main import *

class TestDivide(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(20, 5), 0)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 5), 0)
        self.assertEqual(remainder(0, -5), 0)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)

    def test_divisor_greater_than_dividend(self):
        self.assertEqual(remainder(3, 10), 3)

if __name__ == '__main__':
   unittest.main()
