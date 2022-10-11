# Demo unittest trong Python lần này là sẽ đi kiểm tra xem
# tại vị trí thứ mấy trong dãy số Fibonacci có giá trị bằng bao nhiêu
# Index:         0 1 2 3 4 5 6  ...
# Dãy Fibonacci: 1 1 2 3 5 8 13 ...
# ví dụ: tại vị trí thứ 1 trong dãy số sẽ có giá trị là 1
#                       2       -----------------       2
#                                      ...
#                       4       -----------------       5

import unittest     # unittest là module đã được cài đặt cùng với cài đặt của Python.
import fibonacci    # import file fibonacci.py
import xmlrunner
import io
# unittest cung cấp một class unittest.TestCase
class TestFibo(unittest.TestCase):
    
    #Test case #1: Fibo(4) --> expected: 5  | Vị trí thứ 4 trong dãy số Fibonacci có value là 5
    def test_fibo_value_at_index_4(self):       # các function đều bắt đầu bằng test_
        self.assertEqual(fibonacci.Fibo(4),5)   # assertEqual, assertRaises: Các function dùng để 
                                                # so sánh và raise lên các message thông báo
                                                # cho kết quả test chính xác hay không.
    
    #Test case #2: Fibo(3) --> expected: 3 
    def test_fibo_value_at_index_3(self):
        self.assertEqual(fibonacci.Fibo(3),3)
        
    #Test case #3: Fibo(2) --> expected: 1 (KỲ VỌNG SAI)
    def test_fibo_value_at_index_2(self):    
        self.assertEqual(fibonacci.Fibo(2),1)
        
    #Test case #4: Kiểm tra ngoại lệ khi đưa data sai
    #              Fibonacci ko thể nhập index âm
    #              Nếu nhập data sai sẽ có thông báo Exception
    #              Và nếu có quăng Exception thì
    #              test sẽ pass (ok) | ngược lại: FAIL
    def test_fibo_value_at_index_negative(self):
        with self.assertRaises(Exception):
            fibonacci.Fibo(5)

# unittest.main(verbosity=2) --> Để khởi chạy các test case trong một module
# cần đặt gọi đến unittest.main() của module đó
out = io.BytesIO()
if __name__ == '__main__':
    
    unittest.main(testRunner= xmlrunner.XMLTestRunner(output=out), 
                  failfast=False , buffer=False, catchbreak=False, exit=False)