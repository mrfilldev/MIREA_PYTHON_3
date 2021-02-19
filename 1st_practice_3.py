import math
def f13(x,y):

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            part1 = (((j ** 7) / 46) + (8 * (i ** 3)))


    for i in range(1, x + 1):
        for j in range(1, y + 1):
            part2 = (14 * (i ** 4)) + math.sin(j)

    res = part1 / 47 - part2
