X, Y = input().split()

X, Y = int(X), int(Y)

win = max([X, Y])
lose = min([X, Y])

if lose + 3 > win:
    print('Yes')
else:
    print('No')
