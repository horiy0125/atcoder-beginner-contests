import sys

R, X, Y = map(int, input().split())

e_distance = (X ** 2 + Y ** 2) ** 0.5

if R > e_distance:
    print(2)
    sys.exit()

count = 0

while e_distance > R:
    e_distance -= R
    count += 1

if e_distance == 0:
    print(count)
else:
    print(count+1)
