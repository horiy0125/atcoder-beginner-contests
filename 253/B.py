H, W = map(int, input().split())

P = []

for h in range(H):
    s = input()

    for w in range(len(s)):
        l = s[w]

        if l == 'o':
            P.append([w, h])

print(abs(P[0][0] - P[1][0]) + abs(P[0][1] - P[1][1]))
