H, W = map(int, input().split())

input_squares = []

for h in range(H):
    try:
        row = input()
        input_squares.append(row)
    except EOFError:
        pass


blacks = []
for row in input_squares:
    count = 0
    for letter in row:
        if letter == '#':
            count += 1
    blacks.append(count)
    count = 0

print(sum(blacks))

if sum(blacks) == (H-1) * (W-1):
    print(4)