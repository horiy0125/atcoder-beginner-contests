import itertools

N, M, Q = input().split()
N, M, Q = int(N), int(M), int(Q)

cases = []
for q in range(Q):
    ai, bi, ci, di = input().split()
    ai, bi, ci, di = int(ai), int(bi), int(ci), int(di)
    cases.append([ai, bi, ci, di])

scores = []
for A in itertools.combinations_with_replacement(range(1, M+1), N):
    score = 0
    for case in cases:
        ai, bi, ci, di = case[0], case[1], case[2], case[3]
        if A[bi - 1] - A[ai - 1] == ci:
            score += di

    scores.append(score)

print(max(scores))