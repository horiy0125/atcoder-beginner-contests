import sys

A, B, C, D = map(int, input().split())

blue = A
red = 0

count = 0

while True:
    if blue <= red * D:
        print(count)
        sys.exit()

    if B >= C * D:
        print(-1)
        sys.exit()

    blue += B
    red += C
    count += 1
