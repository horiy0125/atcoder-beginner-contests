N = int(input())

mountains = []

for _ in range(N):
    S, T = input().split()
    T = int(T)

    mountains.append([S, T])

_mountains = sorted(mountains, key=lambda x: x[1], reverse=True)

print(_mountains[1][0])
