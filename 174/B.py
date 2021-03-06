dists = []

N, D = input().split()
N = int(N)
D = int(D)

for i in range (0, N):
  X, Y = input().split()
  dist = int(X)**2 + int(Y)**2
  dists.append(dist)

compare = D**2
count = 0
ans = 0

while count < N:
  if dists[count] <= compare:
    ans += 1
  count += 1
print(ans)
