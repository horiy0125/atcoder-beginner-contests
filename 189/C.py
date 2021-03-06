import itertools

N = int(input())
oranges = input().split()

numbers = []

for i in range(len(oranges)):
    numbers.append(i)
    oranges[i] = int(oranges[i])

com = itertools.product(numbers, repeat=2)

sums = []

for c in com:
    if c[1]+1 > c[0]:
        minimum = min(oranges[c[0]:c[1]+1])
        sums.append(minimum * (c[1] + 1 - c[0]))

print(max(sums))
