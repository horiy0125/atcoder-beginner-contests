x, y = map(int, input().split())

others = [x, y]
if x == y:
    print(x)
elif 0 in others and 1 in others:
    print(2)
elif 1 in others and 2 in others:
    print(0)
else:
    print(1)
