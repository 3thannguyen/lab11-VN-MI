import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################


    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(4,5), 20)
        self.assertEqual(mul(5,6), 30)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 20), 4)
        self.assertEqual(div(6, 30), 5)
        self.assertEqual(div(7, 42), 6)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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