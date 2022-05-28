import math
n=int(input())
dilyatsa = []
for i in range(1,n+1):
    if (i%7)!=0:
        dilyatsa.append(i)
product = math.prod(dilyatsa)
print(product)