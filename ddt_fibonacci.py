import io
import unittest  # unittest là module đã được cài đặt cùng với cài đặt của Python.
from ddt import ddt, file_data
import fibonacci  # import file fibonacci.py
@ddt
class TestFibo(unittest.TestCase): 
    @file_data("data_fibonacci.json")   
    def test_fibo_value_at_index_4(self, e, a):      
        self.assertEqual(fibonacci.Fibo(e), a)   
        