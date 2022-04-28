import sys

S = input()
T = input()

if S == T:
    print('Yes')
    sys.exit()

answer = 'No'


for n in range(len(S) - 1):
    _S = ''
    for m in range(len(S)):
        if m == n:
            _S += S[m+1]
        elif m == n+1:
            _S += S[m-1]
        else:
            _S += S[m]

    if _S == T:
        answer = 'Yes'
        break

print(answer)
