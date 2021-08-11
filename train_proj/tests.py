

import math

x = float(input("Введите значение х: "))
pi = math.pi
y = None

if -pi <= x and x <= pi:
    y = math.cos(3 * x)
elif x < -pi or x > pi:
    y = x

if y == None:
    pass
else:
    print(f'Значение вункции будет: {y}')