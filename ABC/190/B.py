N, S, D = map(int, input().split())

possible = False

for n in range(N):
    X, Y = map(int, input().split())
    if X < S and Y > D:
        possible = True
        break

if possible:
    print('Yes')
else:
    print('No')
