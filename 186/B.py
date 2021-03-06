H, W = input().split()
H, W = int(H), int(W)

blocks = []

for i in range(H):
    row = input().split()
    for r in row:
        blocks.append(int(r))

minimum = min(blocks)
answer = 0

for block in blocks:
    answer += block - minimum

print(answer)
