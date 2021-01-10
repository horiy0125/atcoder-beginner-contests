N, C = input().split()
N, C = int(N), int(C)

change_days = []
costs = []

for i in range(N):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    change_days.append([a, b])
    costs.append(c)

changes = []

for i in range(len(change_days)):
    plus = change_days[i][0]
    minus = change_days[i][1]

    amount = costs[i]

    changes.append([plus, amount])
    changes.append([minus, -amount])


changes.sort(key=lambda x: x[0])

cost = 0
summary = 0

same = False
same_cost = 0

for i in range(len(changes) - 1):
    this = changes[i]
    next = changes[i+1]
    cost += this[1]

    during = next[0] - this[0]
    if during == 0:
        same = True
        same_cost += cost
        pass
    elif during != 0 and same:
        same = False
    if cost > C:
        summary += during*C
    else:
        summary += during * cost

print(summary)
