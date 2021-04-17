import sys

N, P = map(int, input().split())

if P == 2:
    if N == 1:
        print(1)
    else:
        print(0)
    sys.exit()
