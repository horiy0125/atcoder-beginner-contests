N = int(input())
tree = list(map(int, input().split()))

count = 0

for t in tree:
    if t > 10:
        count += t - 10

print(count)
