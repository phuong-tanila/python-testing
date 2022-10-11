# quation.py
def find_x(a, b, c):
    delta = pow(b,2) - (4 * a * c)
    if a != 0 and b != 0 and c != 0:
        if delta > 0:
            return "PT có 2 nghiệm phân biệt"
        elif delta == 0:
            return "PT có nghiệm kép"
        else:
            return "PT vô nghiệm"
    elif a == 0 and b != 0 and c != 0:
        return "PT có 1 nghiệm"
    elif a == 0 and b == 0 and c != 0:
        return "PT vô nghiệm"
    else:
        return "PT có vô số nghiệm"


# print(find_x(1, -3, 2)) # 2 nghiệm phân biệt
# print(find_x(1, -2, 1)) # PT có nghiệm kép
# print(find_x(1, 2, 3))  # PT vô nghiệm

# print(find_x(0, 2, 3))
# print(find_x(0, 0, 3))
# print(find_x(0, 0, 0))

expected = "PT có 2 nghiệm phân biệt"
print("#1 status: expected = " + expected + " | actual = " + find_x(1, -3, 2))

print("#2 status: expected = PT có nghiệm kép" + " | actual = " + find_x(1, -2, 1))

print("#3 status: expected = PT vô nghiệm" + " | actual = " + find_x(1, 2, 3))


