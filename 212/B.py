password = input()


is_strong = True

p = password[0]

if p*4 == password:
    is_strong = False

_password = ''
_p = p
for i in range(4):
    _p = int(_p)

    if _p == 10:
        _password += '0'
        _p = 0
    else:
        _password += str(_p)

    _p = _p + 1


if password == _password:
    is_strong = False

if is_strong:
    print('Strong')
else:
    print('Weak')
