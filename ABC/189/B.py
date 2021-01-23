import sys

N, X = input().split()
N, X = int(N), int(X)

amount = 0

for n in range(1, N+1):
    V, P = input().split()
    V, P = int(V), int(P)

    print(V * P / 100)
    amount += V * P / 100

    if amount > X:
        print(n)
        sys.exit()

print(-1)
