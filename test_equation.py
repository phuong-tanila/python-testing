# test_first_equation.py

import unittest
import equation
import pytest


# def test_find_x1():
#     args = (1, -3, 2)
#     assert equation.find_x(
#         *args) == "Phương trình có  nghiệm phân biệt X1 = -1.0, X2 = -2.0"


# def test_find_x2():
#     args = (1, -3, 2)
#     assert equation.find_x(
#         *args) == "Phương trình có 2 nghiệm phân biệt X1 = -1.0, X2 = -2.0"

class TestFirst(unittest.TestCase):
    def test_find_x_test_case_1(self):
        args = (1, 1, 1)
        self.assertEqual(equation.find_x(*args), "Phương trình vô nghiệm")

    def test_find_x_test_case_2(self):
        args = (1, -4, 4)
        self.assertEqual(equation.find_x(*args),
                         "Phương trình có nghiệm kép X1 = X2 =  2.0")

    def test_find_x_test_case_3(self):
        args = (1, 2, -3)
        self.assertEqual(equation.find_x(
            *args), "Phương trình có 2 nghiệm phân biệt X1 = 3.0, X2 = -1.0")


# if __name__ == '__main__':
#     unittest.main()
