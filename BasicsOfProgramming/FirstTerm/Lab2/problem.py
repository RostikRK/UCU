import math
from math import pi
r = float(input("Введіть радіус основи: "))
h = float(input("Введіть висоту: "))
Obem = h*pi*r**2
Plosch = (h*2*pi*r)+(2*pi*r**2)
print(f'V = {round(Obem, 3)}')
print(f'A = {round(Plosch, 3)}')