import math

N = int(input())
xs = input().split()

manhattan = 0
euclid = 0
chebyshev = []

for x in xs:
    x = int(x)
    if x < 0:
        x = -x

    manhattan += x
    euclid += x ** 2
    chebyshev.append(x)

print(manhattan)
print(math.sqrt(euclid))
print(max(chebyshev))
