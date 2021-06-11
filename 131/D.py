N = int(input())

works = []
for n in range(N):
    A, B = map(int, input().split())
    works.append([A, B])

_works = sorted(works, key=lambda x: x[1])
can_done = True
time = 0

for work in _works:
    A = work[0]
    B = work[1]

    time += A
    if time > B:
        can_done = False
        break

if can_done:
    print('Yes')
else:
    print('No')
