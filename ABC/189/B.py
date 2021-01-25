import sys

N, X = input().split()
N, X = int(N), int(X)

amount = 0

for n in range(1, N+1):
    V, P = input().split()
    V, P = int(V), int(P)

    amount += V * P

    if amount > X * 100:
        print(n)
        sys.exit()

print(-1)
