# quation.py
def find_x(a, b, c):
    delta = pow(b, 2) - (4 * a * c)
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        return "Phương trình có nghiệm kép X1 = X2 = " + str(-b/(2*a))
    else:
        import math
        x1 = str((-b - math.sqrt(delta))/(-2*a))
        x2 = str((-b + math.sqrt(delta))/(-2*a))
        return "Phương trình có 2 nghiệm phân biệt X1 = " + x1 + ", X2 = " + x2


expected = "Phương trình vô nghiệm"
print("#1 status: expected = " + expected + " | actual = " + find_x(1, 1, 1))
expected = "Phương trình có 2 nghiệm phân biệt X1 = -1.0, X2 = -2.0"
print("#2 status: expected = " + expected + " | actual = " + find_x(1, -3, 2))
expected = "Phương trình có nghiệm kép X1 = X2 = 2.0"
print("#3 status: expected = " + expected + " | actual = " + find_x(1, -4, 4))
