N = int(input())
A = list(map(int, input().split()))

count = {}

for a in A:
    count[a] = 0

for a in A:
    count[a] += 1

_A = set(A)
_A = list(_A)

counts = []

for a in _A:
    counts.append(count[a])

answer = 0

for c in counts:
    answer += (N - c) * c

print(int(answer/2))
