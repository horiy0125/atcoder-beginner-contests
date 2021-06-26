import itertools

N = int(input())

li = []

for n in range(N):
    t, l, r = map(int, input().split())
    li.append([t, l, r])

count = 0

com = list(itertools.combinations(li, 2))

for _c in com:
    c1 = _c[0]
    c2 = _c[1]

    t1, l1, r1 = c1
    t2, l2, r2 = c2

    if r1 >= r2:
        if l1 < r2:
            count += 1
            pass
        if l1 == r2:
            co1 = t1 == 1 or t1 == 2
            co2 = t2 == 1 or t2 == 3
            if co1 or co2:
                count += 1
                pass
    else:
        if l2 < r1:
            count += 1
            pass
        if l2 == r1:
            co1 = t2 == 1 or t2 == 2
            co2 = t1 == 1 or t1 == 3
            if co1 or co2:
                count += 1
                pass

print(count)
