N = int(input())

history = []

for i in range(N):
    numbers = []

    L = i + 1

    for j in range(L):
        if j == 0 or j == i:
            numbers.append(1)
        else:
            numbers.append(history[i-1][j-1] + history[i-1][j])

    _numbers = map(str, numbers)
    output = ' '.join(_numbers)
    print(output)
    history.append(numbers)
