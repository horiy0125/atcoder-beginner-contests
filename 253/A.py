a, b, c = map(int, input().split())

l = [a, b, c]
sl = sorted([a, b, c])


if l[1] == sl[1]:
    print('Yes')
else:
    print('No')
