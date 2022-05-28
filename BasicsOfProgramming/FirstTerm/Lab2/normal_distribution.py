import math
from math import sqrt
from math import pi
from math import e
from math import pow
x=float(input())
u=float(input())
o=float(input())
Func=float((1/sqrt(2*pi*pow(o,2)))*pow(e,-((pow(x-u,2))/(2*pow(o,2)))))
print(f'{Func:.10f}')