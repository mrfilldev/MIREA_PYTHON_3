import math
def f13(x,y):


    if x < 160:
        ans = (x ** 8) - (x ** 7)
    elif 160 <= x < 193:
        ans = math.tg((x ** 3 - x ** 4 - 75) + 5 * x ** 5 - 77)
    elif 193 <= x < 262:
        ans = (11 * (x ** 7)) - (21 * (x ** 6))
    elif x >= 262:
        ans = (42*((x ** 5 + x * 8 + 55) ** 7) - 71 * (x ** 3))

