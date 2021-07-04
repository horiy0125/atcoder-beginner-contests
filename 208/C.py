N, K = map(int, input().split())
a = list(map(int, input().split()))

_a = sorted(a)

people = {}
for n in _a:
    people[n] = 0

rate = K / N

if rate > 1:
    for n in _a:
        people[n] += int(rate)
        K -= int(rate)

rate = K / N

if rate > 1:
    for n in _a:
        people[n] += int(rate)
        K -= int(rate)

count = 0
for _ in range(K):
    if K > 0:
        people[_a[count]] += 1
        K -= 1
        count += 1
    else:
        break

for n in a:
    print(people[n])
