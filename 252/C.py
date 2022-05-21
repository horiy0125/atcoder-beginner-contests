N = int(input())

arr = []

for n in range(N):
    S = input()

    reel = []
    for s in S:
        reel.append(int(s))

    arr.append(reel)

results = []

for target in range(10):
    seconds = dict()

    for i in range(10):
        seconds[i] = 0

    for reel in range(N):
        i = arr[reel].index(target)
        seconds[i] += 1

    c = []

    for second in seconds:
        if seconds[second] > 1:
            c.append((seconds[second] - 1) * 10 + second)
        elif seconds[second] == 1:
            c.append(second)

    results.append(max(c))


print(min(results))
