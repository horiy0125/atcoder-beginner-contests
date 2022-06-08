N, K = map(int, input().split())
A = list(map(int, input().split()))

_A = sorted(A)

d = []
for k in range(K):
    d.append([])

for n in range(N):
    mod = n % K
    d[mod].append(A[n])

for k in range(K):
    d[k].sort()

m = []
for n in range(N):
    mod = n % K
    m.append(d[mod].pop(0))

if m == _A:
    print("Yes")
else:
    print("No")
