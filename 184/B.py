N, X = input().split()

N = int(N)
X = int(X)

results = input()

for result in results:
    if result == 'o':
        X += 1
    else:
        if X != 0:
            X -= 1

print(X)
