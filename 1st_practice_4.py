import math

n = int(input('Vvedite N'))

f_1 = 3
for i in range(1, n+1):
    f = (((1 / 13) * (f_1 ** 3)) - ((1 / 38) * (f_1 ** 2)))
    f_1 = f

print(f - 1)
