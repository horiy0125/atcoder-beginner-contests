N = int(input())
A = list(map(int, input().split()))

A.sort()

possible = True

for n in range(N):
    _n = A[n]
    n += 1
    if n != _n:
        possible = False
        break

if possible:
    print('Yes')
else:
    print('No')
