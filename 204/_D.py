# TODO: review C and D
N = int(input())
T = list(map(int, input().split()))

remaining = sorted(T)

oven_1 = 0
oven_2 = 0

while len(remaining) != 0:
    minimum = min(remaining)

    for n in range(len(remaining)):
        remaining[n] = remaining[n] - minimum
        oven_1 += minimum / 2
        oven_2 += minimum / 2

    remaining = remaining[1:]

answer = oven_1

if type(answer) == float:
    answer = int(answer-0.5)
else:
    answer = int(answer)

if answer < max(T):
    print(max(T))
else:
    print(answer)
