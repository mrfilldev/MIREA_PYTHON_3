import math


def f14(n):
    f_2 = 3
    f_1 = 3
    f = 0
    for i in range(1, n + 1):
        f = (((1 / 13) * (f_2 ** 3)) - ((1 / 38) * (f_1 ** 2)))
        f_2 = f_1
        f_1 = f
    return f


#print(f14(3))