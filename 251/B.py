N, W = map(int, input().split())

A = list(map(int, input().split()))

n = []

for a in A:
    n.append(a)

for a in range(N):
    for b in range(N):
        if a != b:
            n.append(A[a]+A[b])


if N >= 3:
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if a != b and b != c and c != a:
                    n.append(A[a]+A[b]+A[c])


a = []
for num in n:
    if num <= W:
        a.append(num)

print(len(set(a)))
