N, X = map(int, input().split())

A = map(int, input().split())

_A = []

for a in A:
    if a != X:
        _A.append(a)

if len(_A) == 0:
    print('')
else:
    for a in _A:
        print(a, end=' ')
