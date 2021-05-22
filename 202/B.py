S = input()

S = S[::-1]

_S = ''
for s in S:
    if s == '6':
        _S += '9'
    elif s == '9':
        _S += '6'
    else:
        _S += s

print(_S)
