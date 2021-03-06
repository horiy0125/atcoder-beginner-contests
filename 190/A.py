A, B, C = map(int, input().split())


if A > B:
    winner = 'Takahashi'
elif A < B:
    winner = 'Aoki'
else:
    if C == 0:
        winner = 'Aoki'
    else:
        winner = 'Takahashi'

print(winner)
