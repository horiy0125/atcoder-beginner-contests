import math

X, Y, R = map(float, input().split())

candidates = []

left = math.ceil(X - R)
right = math.floor(X + R)
top = math.floor(Y + R)
bottom = math.ceil(Y - R)

out_count = 0

for x in range(left, right + 1):
    for y in range(bottom, top + 1):
        if x ** 2 + y ** 2 > R ** 2:
            out_count += 1
        else:
            break

for x in range(right + 1, left):
    for y in range(bottom, top + 1):
        if x ** 2 + y ** 2 > R ** 2:
            out_count += 1
        else:
            break

for x in range(left, right + 1):
    for y in range(top + 1, bottom):
        if x ** 2 + y ** 2 > R ** 2:
            out_count += 1
        else:
            break

for x in range(right + 1, left):
    for y in range(top + 1, bottom):
        if x ** 2 + y ** 2 > R ** 2:
            out_count += 1
        else:
            break

square_num = (right - left + 1) * (top - bottom + 1)
print(square_num - out_count)
