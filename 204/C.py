import sys

N, M = map(int, input().split())

if M == 0:
    print(N)
    sys.exit()

roads = {}

for n in range(N):
    roads[n+1] = []

for n in range(N):
    A, B = map(int, input().split())
    roads[A].append(B)

print(roads)
