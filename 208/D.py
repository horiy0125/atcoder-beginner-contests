N, M = map(int, input().split())

d = {}
roads = {}

for n in range(N):
    d[n] = []
    roads[n] = []

for m in range(M):
    A, B, C = map(int, input().split())
    d[A].append([B, C])
    roads[A].append(B)

ans = 0

for s in range(N):
    for t in range(N):
        for k in range(1, N+1):
            if s == t:
                pass
