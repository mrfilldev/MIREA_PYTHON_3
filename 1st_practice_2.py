import math


def f12(x):
    if x < 160:
        ans = (x ** 8) - (x ** 7)
    elif 160 <= x < 193:
        ans = math.tan((pow(x, 3) - pow(x, 4) - 75)) + (5 * (pow(x, 5))) - 77
    elif 193 <= x < 262:
        ans = (50 * (pow((math.cos(x) + 70 * pow(x, 6)), 6))) + (abs(x))
    elif x >= 262:

        a = pow(x, 5)
        b = pow(x, 8)
        c = pow(x, 3)
        #d = pow((a + b + c), 7)
        #e = 42 * (d + 55)
       # ans = e - (71 * c)
        ans = 42 * pow((a + b + 55), 7) - 71 * c
    return ans


print(f12(268))
print(f12(194))
print(f12(191))
print(f12(150))
print(f12(177))


