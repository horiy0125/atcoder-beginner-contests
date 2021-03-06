import itertools

N = int(input())

A = input().split()

square = 0

for a in A:
    square += int(a) ** 2

square *= 2

combinations = itertools.combinations(A, 2)

product = 0

for c in combinations:
    product += int(c[0]) * int(c[1])

product *= -2

print(square + product)
