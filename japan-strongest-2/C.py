import math
import sys

A, B = map(int, input().split())

diff = B - A

if diff == 1:
    print(1)
    sys.exit()
else:
    multiple = None
    for n in range(diff, 0, -1):
        upper = int(B / n)
        lower = math.ceil(A / n)

        if upper != lower:
            multiple = n
            break

    print(multiple)
