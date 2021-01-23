N, C = input().split()
N, C = int(N), int(C)

change_days = []
costs = []

for i in range(N):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    change_days.append([a-1, b])
    costs.append(c)

changes = []

for i in range(len(change_days)):
    plus = change_days[i][0]
    minus = change_days[i][1]

    amount = costs[i]

    changes.append([plus, amount])
    changes.append([minus, -amount])


changes.sort(key=lambda x: x[0])


start = changes[0][0]
end = changes[len(changes) - 1][0]

days = [0] * (end - start + 1)

for i in range(len(changes)):
    day = changes[i][0]
    change = changes[i][1]

    days[day] += change


summary = 0
current = 0

for cost in days[:len(days) - 1]:
    current += cost
    if current > C:
        summary += C
    else:
        summary += current

print(summary)
