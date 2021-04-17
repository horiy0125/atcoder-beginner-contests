X, Y, Z = map(int, input().split())

if X == Z:
    answer = Y - 1
else:
    tak_net = Y / X
    tak_equal = Z * tak_net

    _tak_equal = int(tak_equal)

    if tak_equal == _tak_equal:
        answer = _tak_equal - 1
    else:
        answer = _tak_equal

print(answer)
