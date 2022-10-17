import unittest
import equation

from ddt import ddt, data, file_data, unpack


@ddt
class TestFirst(unittest.TestCase):
    @file_data("../python-testing-main/test_equation_data.json")
    def test_find_x(self, a, b, c, result):
        args = (a, b, c)
        self.assertEqual(equation.find_x(*args), result)
