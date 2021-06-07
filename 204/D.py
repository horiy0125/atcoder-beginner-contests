import sys


N = int(input())
T = list(map(int, input().split()))

if len(T) == 1:
    print(T[0])
    sys.exit()
elif len(T) == 2:
    print(max(T))
    sys.exit()

remaining = sorted(T)

oven_1 = 0
oven_2 = 0

while len(remaining) != 0:
    minimum = min(remaining)

    print(remaining)
    print(oven_1, oven_2)
    for n in range(len(remaining)):
        if len(remaining) == 1:
            if oven_1 > oven_2:
                oven_2 += remaining[0]
                break
            else:
                oven_1 += remaining[0]
                break
        else:
            remaining[n] = remaining[n] - minimum
            oven_1 += minimum / 2
            oven_2 += minimum / 2

    remaining = remaining[1:]

answer = max([oven_1, oven_2])

if type(answer) == float:
    print(int(answer-0.5))
else:
    print(int(answer))
