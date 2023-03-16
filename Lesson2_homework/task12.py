x_number = 12
y_number = 10

s_xy = x_number+y_number
p_xy = x_number*y_number
_break = False

for i in range(1001):
    for j in range(1001):
        if i+j == s_xy and i*j == p_xy:
            _break = True
            print(f"Задуманные числа X: {i}, Y: {j}")
            break
    if _break:
        break
