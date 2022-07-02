N = int(input())

board = []
max_num = 0
max_position = None

for n in range(N):
    raw_row = input()
    row = []

    for m in range(N):
        num = int(raw_row[m])
        row.append(num)

        if num > max_num:
            max_num = num
            max_position = [m, n]

    board.append(row)

nums = []
initial_position = max_position

position = None
num = str(max_num)
for i in range(1, N):
    m = initial_position[0]
    n = initial_position[1]

    position = [m, n - i]

    if position[1] < 0:
        position[1] += N
    elif position[1] > N-1:
        position[1] -= N

    num += str(board[position[0]][position[1]])

nums.append(int(num))

position = None
num = str(max_num)
for i in range(1, N):
    m = initial_position[0]
    n = initial_position[1]

    position = [m, n + i]

    if position[1] < 0:
        position[1] += N
    elif position[1] > N-1:
        position[1] -= N

    num += str(board[position[0]][position[1]])

nums.append(int(num))

position = None
num = str(max_num)
for i in range(1, N):
    m = initial_position[0]
    n = initial_position[1]

    position = [m - i, n]

    if position[0] < 0:
        position[0] += N
    elif position[0] > N-1:
        position[0] -= N

    num += str(board[position[0]][position[1]])

nums.append(int(num))

position = None
num = str(max_num)
for i in range(1, N):
    m = initial_position[0]
    n = initial_position[1]

    position = [m + i, n]

    if position[0] < 0:
        position[0] += N
    elif position[0] > N-1:
        position[0] -= N

    num += str(board[position[0]][position[1]])

nums.append(int(num))

position = None
num = str(max_num)
for i in range(1, N):
    m = initial_position[0]
    n = initial_position[1]

    position = [m - i, n - i]

    if position[0] < 0:
        position[0] += N
    elif position[0] > N-1:
        position[0] -= N

    if position[1] < 0:
        position[1] += N
    elif position[1] > N-1:
        position[1] -= N

    num += str(board[position[0]][position[1]])

nums.append(int(num))

position = None
num = str(max_num)
for i in range(1, N):
    m = initial_position[0]
    n = initial_position[1]

    position = [m + i, n - i]

    if position[0] < 0:
        position[0] += N
    elif position[0] > N-1:
        position[0] -= N

    if position[1] < 0:
        position[1] += N
    elif position[1] > N-1:
        position[1] -= N

    num += str(board[position[0]][position[1]])

nums.append(int(num))

position = None
num = str(max_num)
for i in range(1, N):
    m = initial_position[0]
    n = initial_position[1]

    position = [m - i, n + i]

    if position[0] < 0:
        position[0] += N
    elif position[0] > N-1:
        position[0] -= N

    if position[1] < 0:
        position[1] += N
    elif position[1] > N-1:
        position[1] -= N

    num += str(board[position[0]][position[1]])

nums.append(int(num))

position = None
num = str(max_num)
for i in range(1, N):
    m = initial_position[0]
    n = initial_position[1]

    position = [m + i, n + i]

    if position[0] < 0:
        position[0] += N
    elif position[0] > N-1:
        position[0] -= N

    if position[1] < 0:
        position[1] += N
    elif position[1] > N-1:
        position[1] -= N

    num += str(board[position[0]][position[1]])
    print(num)

nums.append(int(num))

print(max(num))
