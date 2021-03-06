V, T, S, D = map(int, input().split())

vanish_start = V * T
vanish_end = V * S

if D > vanish_end or D < vanish_start:
    print('Yes')
else:
    print('No')
