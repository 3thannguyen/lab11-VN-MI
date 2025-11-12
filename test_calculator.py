# https://github.com/3thannguyen/lab11-VN-MI
# Partner 1: Ethan Nguyen
# Partner 2: Mahir Isic

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(100, 200), 300)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 5), 0)
        self.assertEqual(sub(-5, 5), -10)
        self.assertEqual(sub(100, 200), -100)


    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(4,5), 20)
        self.assertEqual(mul(5,6), 30)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 20), 4)
        self.assertEqual(div(6, 30), 5)
        self.assertEqual(div(7, 42), 6)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(8, 2), 3)
        self.assertEqual(log(4, 2), 2)
        self.assertEqual(log(64, 8), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 3)
    
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(50, 0)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(7, 24), 25)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()