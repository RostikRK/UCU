import math
from math import sqrt
m=float(input(""))
V_s=float(input(""))
Con=float(299792458.0)
mr=m/sqrt(1-((V_s**2) / (Con**2)))
E=mr*Con**2
print(E)