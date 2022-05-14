S = input()

N = set()

for i in range(10):
    N.add(i)

L = set()

for l in S:
    L.add(int(l))

diff = N - L

print(list(diff)[0])
