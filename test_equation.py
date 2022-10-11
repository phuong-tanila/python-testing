# test_first_equation.py

import unittest
import equation

class TestFirst(unittest.TestCase):

    def test_find_x(self):
        args = (1, -3, 2)
        self.assertEqual(equation.find_x(*args), "P có 2 nghiệm phân biệt")


if __name__ == '__main__':
    unittest.main(verbosity=2)