N = int(input())

poems = []
scores = []
for n in range(N):
    poem, score = input().split()
    poems.append(poem)
    scores.append(int(score))

d = {}
for n in range(N):
    d[poems[n]] = None

for n in range(N):
    if d[poems[n]] == None:
        d[poems[n]] = [n, scores[n]]

hs = 0
idx = N+1


for p in set(poems):
    if d[p][1] >= hs:
        if d[p][1] == hs:
            if d[p][0] < idx:
                idx = d[p][0]
                hs = d[p][1]
        else:
            idx = d[p][0]
            hs = d[p][1]

print(idx+1)
