N = int(input())
A = []
data = input().split()

for i in range(N):
    A.append(int(data[i]))


def moving(positions, A, trial):
    trial += 1
    if trial == len(A) + 1:
        print(max(positions))
    else:
        moves = A[0: trial]
        for move in moves:
            latest = len(positions) - 1
            new_position = positions[latest] + move
            positions.append(new_position)
        moving(positions, A, trial)


positions = moving([0], A, 0)
