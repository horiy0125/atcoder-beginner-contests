import itertools

N, M = map(int, input().split())

conditions = []

for m in range(M):
    A, B = map(int, input().split())
    conditions.append([A, B])


K = int(input())
balls = []

for k in range(K):
    C, D = map(int, input().split())
    balls.append([C, D])

conditions.sort(key=lambda x: x[0])
balls.sort(key=lambda x: x[0])

patterns = list(itertools.product([0, 1], repeat=len(balls)))

counts = []

for pattern in patterns:
    dishes = [0] * N
    for person in range(len(balls)):
        number = balls[person][pattern[person]] - 1
        dishes[number] += 1

    count = 0

    for condition in conditions:
        first = condition[0]
        second = condition[1]

        if dishes[first - 1] > 0 and dishes[second - 1] > 0:
            count += 1

    counts.append(count)

print(max(counts))
