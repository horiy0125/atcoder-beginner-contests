import itertools

N = int(input())

dots = []

for i in range(N):
    x, y = input().split()
    x, y = int(x), int(y)
    dots.append([x, y])

tilts = []

com = list(itertools.combinations(dots, 2))

for i in com:
    tilts.append((i[1][1] - i[0][1]) / (i[1][0] - i[0][0]))

count = 0
for i in tilts:
    if i >= -1 and i <= 1:
        count += 1

print(count)
