import sys

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(0)
    sys.exit()

mid_idx = int(N / 2)
if N % 2 == 0:
    firsts = A[:mid_idx]
    lasts = A[mid_idx:]
else:
    firsts = A[:mid_idx]
    lasts = A[mid_idx+1:]

lasts.reverse()

if firsts == lasts:
    print(0)
else:
    f = []
    l = []

    for i in range(mid_idx):
        _f = firsts[i]
        _l = lasts[i]
        if _f != _l:
            f.append(_f)
            l.append(_l)

    numbers = set(f + l)
    answers = [len(numbers) - 1]
    answers.append(len(f))

    print(min(answers))
