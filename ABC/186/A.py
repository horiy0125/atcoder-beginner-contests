N, W = input().split()
N, W = int(N), int(W)

bricks = 0
weight = 0

while weight <= N:
    bricks += 1
    weight += W

print(bricks - 1)
